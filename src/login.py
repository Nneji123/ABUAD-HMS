from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, login_user
from werkzeug.security import check_password_hash

from schema import Admins

login = Blueprint(
    "login", __name__, template_folder="./templates", static_folder="./templates/static"
)
login_manager = LoginManager()
login_manager.init_app(login)


@login.route("/login", methods=["GET", "POST"])
def show():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = Admins.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("home.show"))
            else:
                flash("Incorrect password. Please try again!", "danger")

                return redirect(
                    url_for("login.show") + "?error=incorrect-password-unauthorized"
                )
        else:
            flash("You are not a registered admin!", "danger")
            return redirect(url_for("login.show") + "?error=user-not-found")
    else:
        return render_template("login.html")
