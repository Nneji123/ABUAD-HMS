import cv2
import torch

import yolov5
from deep_sort.deep_sort import DeepSort
from deep_sort.utils.parser import get_config
from yolov5.utils.general import xyxy2xywh
from yolov5.utils.plots import Annotator, colors
from yolov5.utils.torch_utils import select_device


device = select_device("gpu" if torch.cuda.is_available() else "cpu")
# load model
model = yolov5.load("./models/yolov5n.onnx")
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


def smoking_stream():
    cap = cv2.VideoCapture(0)
    model.conf = 0.2
    model.iou = 0.5
    model.classes = [0]
    while True:
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
