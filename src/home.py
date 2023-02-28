import cv2
from flask import Blueprint, Response, render_template
from flask_login import LoginManager, login_required

from utils import smoking_stream, violence_stream, get_image_files


home = Blueprint("home", __name__, template_folder="./templates")
login_manager = LoginManager()
login_manager.init_app(home)


cap = cv2.VideoCapture(0)
    
@login_required
@home.route("/home")
def show():
    return render_template("index.html")


@login_required
@home.route("/view_offenders")
def view_offenders():
    images = get_image_files("./templates/static/offenders/")
    return render_template("view_offenders.html", images=images)


@login_required
@home.route("/monitor")
def monitor():
    return render_template("monitor.html")


@login_required
@home.route("/smoking_feed")
def smoking_feed():
    return Response(smoking_stream(cap), mimetype="multipart/x-mixed-replace; boundary=frame")

@login_required
@home.route("/violence_feed")
def violence_feed():
    return Response(violence_stream(cap), mimetype="multipart/x-mixed-replace; boundary=frame")