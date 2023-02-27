from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, login_user
from werkzeug.security import check_password_hash

from schema import Users, db

login = Blueprint(
    "login", __name__, template_folder="./templates", static_folder="./templates/static"
)
login_manager = LoginManager()
login_manager.init_app(login)


@login.route("/login", methods=["GET", "POST"])
def show():
    if request.method == "POST":
        # username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        user = Users.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("home.show"))
            else:
                flash("Incorrect password. Please try again.")

                return redirect(
                    url_for("login.show") + "?error=incorrect-password-unauthorized"
                )
        else:
            flash("You are not registered with us. Please register first.")
            return redirect(url_for("login.show") + "?error=user-not-found")
    else:
        return render_template("login.html")
