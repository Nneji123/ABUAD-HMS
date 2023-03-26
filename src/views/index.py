from flask import Blueprint, redirect

index = Blueprint("index", __name__)


@index.route("/", methods=["GET"])
def show():
    return redirect("login")
