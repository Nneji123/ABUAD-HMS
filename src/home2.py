# import os
# import sys
# from pathlib import Path

# import sqlalchemy

# from dotenv import load_dotenv
# from flask import Flask, Response, render_template
# from flask_login import LoginManager

# import torch
# from models.common import DetectMultiBackend
# from utils.dataloaders import LoadStreams
# from utils.general import (Profile, check_img_size, check_imshow, cv2,
#                            increment_path, non_max_suppression, scale_boxes)
# from utils.plots import Annotator, colors, save_one_box
# from utils.torch_utils import select_device, smart_inference_mode

# import sqlalchemy
# from flask import Blueprint, redirect, render_template, request, url_for
# from flask_login import LoginManager


# from deep_sort_realtime.deepsort_tracker import DeepSort

# home = Blueprint("home", __name__, template_folder="./templates")
# login_manager = LoginManager()
# login_manager.init_app(home)


# FILE = Path(__file__).resolve()
# ROOT = FILE.parents[0]  # YOLOv5 root directory
# if str(ROOT) not in sys.path:
#     sys.path.append(str(ROOT))  # add ROOT to PATH
# ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative


# @smart_inference_mode()
# def run( imgsz=(640, 640), conf_thres=0.5, iou_thres=0.45, max_det=1000,  view_img=False,  save_crop=False, visualize=False, line_thickness=2,hide_labels=False, hide_conf=False):
#     source = str(0)
#     # Directories
#     save_dir = increment_path(Path('runs/detect') / 'exp', exist_ok=False)  # increment run

#     # Load model
#     device = select_device("gpu" if torch.cuda.is_available() else "cpu")
#     model = DetectMultiBackend(weights="yolov5n.onnx", device=device)
#     stride, names, pt = model.stride, model.names, model.pt
#     imgsz = check_img_size(imgsz, s=stride)  # check image size

#     # Dataloader
#     view_img = check_imshow(warn=True)
#     dataset = LoadStreams(source, img_size=imgsz, stride=stride, auto=pt, vid_stride=1)


#     seen, windows, dt = 0, [], (Profile(), Profile(), Profile())
#     for path, im, im0s, vid_cap, s in dataset:
#         with dt[0]:
#             im = torch.from_numpy(im).to(model.device)
#             im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
#             im /= 255  # 0 - 255 to 0.0 - 1.0
#             if len(im.shape) == 3:
#                 im = im[None]  # expand for batch dim

#         # Inference
#         with dt[1]:
#             visualize = increment_path(save_dir / Path(path).stem, mkdir=True) if visualize else False
#             pred = model(im, augment=False, visualize=visualize)

#         # NMS
#         with dt[2]:
#             pred = non_max_suppression(pred, conf_thres, iou_thres, classes=None,  max_det=max_det)
#         # Process predictions
#         for i, det in enumerate(pred):  # per image
#             seen += 1
#             p, im0= path[i], im0s[i].copy()
#             s += f'{i}: '


#             p = Path(p)  # to Path
#             s += '%gx%g ' % im.shape[2:]  # print string
#             imc = im0.copy() if save_crop else im0  # for save_crop
#             annotator = Annotator(im0, line_width=line_thickness, example=str(names))
#             tracker = DeepSort(embedder_gpu=False)
#             tracks = tracker.update_tracks(pred, frame=imc)

#             if len(det):
#                     # Checking if tracks exist.
#                 for track in tracks:
#                     if not track.is_confirmed() or track.time_since_update > 1:
#                         continue
#                         # Changing track bbox to top left, bottom right coordinates
#                     det = [int(position) for position in list(track.to_tlbr())]
#                 # Rescale boxes from img_size to im0 size
#                 det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()

#                 # Print results
#                 for c in det[:, 5].unique():
#                     n = (det[:, 5] == c).sum()  # detections per class
#                     s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

#                 # Write results
#                 for *xyxy, conf, cls in reversed(det):
#                     if save_crop or view_img:  # Add bbox to image
#                         c = int(cls)  # integer class
#                         label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
#                         annotator.box_label(xyxy, label, color=colors(c, True))
#                     if save_crop:
#                         save_one_box(xyxy, imc, file=save_dir / 'crops' / names[c] / f'{p.stem}.jpg', BGR=True)

#             # Stream results
#             im0 = annotator.result()

#             image_bytes = cv2.imencode('.jpg', im0)[1].tobytes()
#             yield (b'--frame\r\n'
#                 b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')


# # @login_required
# @home.route("/home")
# def show():
#     return render_template("index.html")

# # @login_required
# @home.route("/video_feed")
# def video_feed():
#     return Response(run(), mimetype="multipart/x-mixed-replace; boundary=frame")
