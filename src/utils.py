import os
import time

import cv2
import numpy as np
import onnxruntime as rt
import torch

import yolov5
from deep_sort.deep_sort import DeepSort
from deep_sort.utils.parser import get_config
from yolov5.utils.general import xyxy2xywh
from yolov5.utils.plots import Annotator, colors
from yolov5.utils.torch_utils import select_device


import threading

# create a lock to synchronize access to the camera
camera_lock = threading.Lock()


# ONNX Initializations
output_path = "./models/violence.onnx"
providers = ["CPUExecutionProvider"]
m = rt.InferenceSession(output_path, providers=providers)

# Image Preprocessing Variables
SEQUENCE_LENGTH = 16
IMAGE_HEIGHT = 64
IMAGE_WIDTH = 64
CLASSES_LIST = ["NonViolence", "Violence"]



device = select_device("gpu" if torch.cuda.is_available() else "cpu")
# load model
model = yolov5.load("./models/smoking_small.onnx")
device = select_device("cpu")  # 0 for gpu, '' for cpu
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
# Get names and colors
names = model.module.names if hasattr(model, "module") else model.names


def smoking_stream(cap):
    # cap = cv2.VideoCapture(0)
    model.conf = 0.6
    model.iou = 0.5
    model.classes = [0]

    while True:
        # acquire the lock before accessing the camera
        camera_lock.acquire()
        success, frame = cap.read()
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
        # print(df)
        count = 0
        for i in df['name']:
            lst.append(i)
            count+=1
            if 'person' in lst:
                # print("This person was caught smoking")
                cv2.imwrite(f"./frame/file_{count}.jpg/", frame)
            else:
                print("No smoking")
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
        p = "test"
        im0 = annotator.result()

        image_bytes = cv2.imencode(".jpg", im0)[1].tobytes()
        yield (
            b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + image_bytes + b"\r\n"
        )



def violence_stream(cap):
    # cap = cv2.VideoCapture(0)
    while True:
        # acquire the lock before accessing the camera
        camera_lock.acquire()
        success, frame = cap.read()
        # release the lock after accessing the camera
        camera_lock.release()
        frames_list = []
        for frame_counter in range(SEQUENCE_LENGTH):
            success, frame = cap.read()
            if not success:
                break
            resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))
            normalized_frame = resized_frame / 255
            frames_list.append(normalized_frame)
        if len(frames_list) < SEQUENCE_LENGTH:
            break
        input_tensor = np.array(frames_list).reshape(
            1, SEQUENCE_LENGTH, IMAGE_HEIGHT, IMAGE_WIDTH, 3
        )
        input_tensor = input_tensor.astype(np.float32)
        onnx_pred = m.run(["dense_4"], {"input": input_tensor})
        predicted_labels_probabilities = onnx_pred[0][0]
        predicted_label = np.argmax(predicted_labels_probabilities)
        predicted_class_name = CLASSES_LIST[predicted_label]
        if predicted_class_name == "Violence":
            image_name = "violence_detected_" + str(int(time.time())) + ".jpg"
            text = "Violence Detected!"
            print("Violence Detected!")
        else:
            text = ""
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.2, 2)[0]
        text_x = int((frame.shape[1] - text_size[0]) / 2)
        text_y = int((frame.shape[0] + text_size[1]) / 2)
        cv2.putText(
            frame,
            text,
            (text_x, text_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
        )
        ret, buffer = cv2.imencode(".jpg", frame)
        new_frame = buffer.tobytes()
        yield (
            b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + new_frame + b"\r\n"
        )
        key = cv2.waitKey(20)
        if key == 27:
            break


def get_image_files(directory):
    """
    Returns a list of all image files (jpg, jpeg, png, gif) in the given directory.
    """
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    image_files = []
    for file in os.listdir(directory):
        if os.path.splitext(file)[1].lower() in image_extensions:
            image_files.append(os.path.join('static/offenders', file))
    return image_files



# def violence_stream(cap):
#     # cap = cv2.VideoCapture(0)
#     while True:
#         # acquire the lock before accessing the camera
#         camera_lock.acquire()
#         success, frame = cap.read()
#         # release the lock after accessing the camera
#         camera_lock.release()

#         text = "Violence Detected!"
#         text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.2, 2)[0]
#         text_x = int((frame.shape[1] - text_size[0]) / 2)
#         text_y = int((frame.shape[0] + text_size[1]) / 2)
#         cv2.putText(
#             frame,
#             text,
#             (text_x, text_y),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             1,
#             (255, 255, 255),
#             2,
#         )
#         ret, buffer = cv2.imencode(".jpg", frame)
#         new_frame = buffer.tobytes()
#         yield (
#             b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + new_frame + b"\r\n"
#         )
#         key = cv2.waitKey(20)
#         if key == 27:
#             break
        
#     # cap.release()

# def smoking_stream(cap):
#     # cap = cv2.VideoCapture(0)
#     while True:
#         # acquire the lock before accessing the camera
#         camera_lock.acquire()
#         success, frame = cap.read()
#         # release the lock after accessing the camera
#         camera_lock.release()

#         text = "Smoking Detected"
#         text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.2, 2)[0]
#         text_x = int((frame.shape[1] - text_size[0]) / 2)
#         text_y = int((frame.shape[0] + text_size[1]) / 2)
#         cv2.putText(
#             frame,
#             text,
#             (text_x, text_y),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             1,
#             (255, 255, 255),
#             2,
#         )
#         ret, buffer = cv2.imencode(".jpg", frame)
#         new_frame = buffer.tobytes()
#         yield (
#             b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + new_frame + b"\r\n"
#         )
#         key = cv2.waitKey(20)
#         if key == 27:
#             break
#     # cap.release()
