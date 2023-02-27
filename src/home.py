import os

from flask import Blueprint, Response, render_template
from flask_login import LoginManager, login_required

from utils import smoking_stream, violence_stream


home = Blueprint("home", __name__, template_folder="./templates")
login_manager = LoginManager()
login_manager.init_app(home)


@login_required
@home.route("/home")
def show():
    return render_template("index.html")


@login_required
@home.route("/smoking_feed")
def smoking_feed():
    return Response(smoking_stream(), mimetype="multipart/x-mixed-replace; boundary=frame")

@login_required
@home.route("/violence_feed")
def violence_feed():
    return Response(violence_stream(), mimetype="multipart/x-mixed-replace; boundary=frame")


@login_required
@home.route("/monitor")
def monitor():
    return render_template("monitor.html")


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




@login_required
@home.route("/view_offenders")
def view_offenders():
    images = get_image_files("./templates/static/offenders/")
    return render_template("view_offenders.html", images=images)
