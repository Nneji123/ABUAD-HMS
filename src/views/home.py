import os
import threading
from datetime import datetime

import cv2
from flask import current_app, render_template
from flask_mail import Message
from jinja2 import Environment, FileSystemLoader
import torch
import torch.nn.functional as F
import yolov5
from yolov5.models.common import DetectMultiBackend
from yolov5.utils.general import xyxy2xywh
from yolov5.utils.plots import Annotator, colors
from yolov5.utils.torch_utils import select_device

from configurations.extensions import email

from deep_sort.deep_sort import DeepSort
from deep_sort.utils.parser import get_config
import cv2
from flask import Blueprint, Response, render_template
from flask_login import login_required


home = Blueprint("home", __name__)


cap = cv2.VideoCapture(0)


# create a lock to synchronize access to the camera
camera_lock = threading.Lock()

save_folder = "./static/offenders/"

model_smoking = yolov5.load("./models/smoking_large.onnx")
model_violence = "./models/violence_yolo.onnx"


device = select_device("gpu" if torch.cuda.is_available() else "cpu")
# initialize deepsort
cfg = get_config()
cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
deepsort = DeepSort(
    "osnet_x0_25",
    device,
    max_dist=cfg.DEEPSORT.MAX_DIST,
    max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
    max_age=cfg.DEEPSORT.MAX_AGE,
    n_init=cfg.DEEPSORT.N_INIT,
    nn_budget=cfg.DEEPSORT.NN_BUDGET,
)

def send_mail(to, template, subject, image, **kwargs):
    """
    The send_mail_flask function is used to send an email from the Flask app.
    It takes in a recipient, template, subject and link as its parameters. It also takes in optional arguments that can be passed into the function.

    :param to: Specify the recipient of the email
    :param template: Specify the html template that will be used to send the email
    :param subject: Set the subject of the email
    :param image: Image offender to be sent
    :param **kwargs: Pass in any additional variables that are needed to be rendered in the email template
    :return: The html of the email that is being sent
    """
    sender = os.getenv("SENDER_EMAIL")
    msg = Message(subject=subject, sender=sender, recipients=[to])
    
    # create Jinja2 environment
    env = Environment(loader=FileSystemLoader(searchpath='templates/'))
    
    # render the template with the given variables
    html = env.get_template(template).render(image=image, **kwargs)
    msg.html = html
    email.send(msg)


def get_image_files(directory):
    """
    Returns a list of all image files (jpg, jpeg, png, gif) in the given directory.
    """
    image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    image_files = []
    for file in os.listdir(directory):
        if os.path.splitext(file)[1].lower() in image_extensions:
            image_files.append(os.path.join("static/offenders", file))
    return image_files


@login_required
@home.route("/home")
def show():
    return render_template("index.html")


@login_required
@home.route("/view_offenders")
def view_offenders():
    images = get_image_files("./static/offenders/")
    return render_template("view_offenders.html", images=images)


@login_required
@home.route("/monitor")
def monitor():
    return render_template("monitor.html")


@login_required
@home.route("/smoking_feed")
def smoking_feed():
    def smoking_stream(cap):
        model = model_smoking
        names = model.module.names if hasattr(model, "module") else model.names
        model.conf = 0.6
        model.iou = 0.5
        model.classes = [0]

        while True:
            # acquire the lock before accessing the camera
            camera_lock.acquire()
            # release the lock after accessing the camera
            camera_lock.release()
            ret, frame = cap.read()
            if not ret:
                print("Error: failed to capture image")
                break

            frame = cv2.resize(frame, (256, 256))
            lst = []
            results = model(frame, augment=True)
            df = results.pandas().xyxy[0]
            count = 0
            for i in df["name"]:
                lst.append(i)
                if (
                    "smoke" in lst
                    and df[df["name"] == "smoke"]["confidence"].iloc[0] >= 0.85
                ):
                    count += 1
                    print("Smoking Detected")
                    filename = f"smoking_detected_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.jpg"

                    cv2.imwrite(
                        os.path.join(save_folder, filename), frame
                    )  # save frame in "smoke_frames" folder
                    # send_mail(
                    #     to=os.getenv("ADMIN_EMAIL"),
                    #     template="email.html",
                    #     subject="Smokers Detected",
                    #     image=filename,
                    # )
                    print("Sent Email")
                else:
                    pass
            # proccess
            annotator = Annotator(frame, line_width=2, pil=not ascii)
            det = results.pred[0]
            if det is not None and len(det):
                xywhs = xyxy2xywh(det[:, 0:4])
                confs = det[:, 4]
                clss = det[:, 5]
                outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
                if len(outputs) > 0:
                    for j, (output, conf) in enumerate(zip(outputs, confs)):
                        bboxes = output[0:4]
                        id = output[4]
                        cls = output[5]

                        c = int(cls)  # integer class
                        label = f"{id} {names[c]} {conf:.2f}"
                        annotator.box_label(bboxes, label, color=colors(c, True))
            else:
                deepsort.increment_ages()
            im0 = annotator.result()

            image_bytes = cv2.imencode(".jpg", im0)[1].tobytes()
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + image_bytes + b"\r\n"
            )
        cap.release()

    return Response(
        smoking_stream(cap), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@login_required
@home.route("/violence_feed")
def violence_feed():
    with current_app.app_context():
        def violence_stream(cap):
            weights = model_violence
            model = DetectMultiBackend(
                weights, device=device, dnn=False, data=None, fp16=False
            )  # load model
            stride, names = model.stride, model.names
            while True:
                camera_lock.acquire()
                ret, frame = cap.read()
                frame = cv2.resize(frame, (256, 256))
                # release the lock after accessing the camera
                camera_lock.release()
                if not ret:
                    break

                im0 = frame.copy()  # original image
                im = cv2.resize(frame, (640, 640))  # resize to 640x640
                im = im[:, :, ::-1]  # BGR to RGB
                im = im.copy()
                im = torch.from_numpy(im).to(device)  # to tensor
                im = im.permute(2, 0, 1).float().div(255.0).unsqueeze(0)  # normalize
                results = model(im)  # inference
                pred = F.softmax(results, dim=1)  # probabilities
                top5i = pred.argsort(1, descending=True)[0, :5].tolist()  # top 5 indices
                top5 = [f"{names[i]} {pred[0, i]:.2f}" for i in top5i]  # top 5 classes
                if "violence" in top5[0] and pred[0, top5i[0]] >= 0.2:
                    filename = f"violence_detected_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.jpg"
                    cv2.putText(
                        frame,
                        ", ".join(top5),
                        (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.4,
                        (0, 255, 0),
                        2,
                    )
                    cv2.imwrite(os.path.join(save_folder, filename), frame)
                    image_path = os.path.join(save_folder, filename)
                    send_mail(
                        to=os.getenv("ADMIN_EMAIL"),
                        template="email.html",
                        subject="Violence Detected",
                        image=image_path,
                    )
                    print("Sent Email")
                cv2.putText(
                    im0,
                    ", ".join(top5),
                    (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.4,
                    (0, 255, 0),
                    2,
                )  # annotate the image
                im0 = cv2.imencode(".jpg", im0)[1].tobytes()
                yield (
                    b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + im0 + b"\r\n"
                )  # encode the image as JPEG and return the bytes
            cap.release()

        return Response(
            violence_stream(cap), mimetype="multipart/x-mixed-replace; boundary=frame"
        )
