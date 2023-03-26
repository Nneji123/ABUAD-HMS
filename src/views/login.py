import sys
from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user
from werkzeug.security import check_password_hash

sys.path.append("..")


from configurations.schema import db, Admins

login = Blueprint("login", __name__)


@login.route("/login", methods=["GET", "POST"])
def show():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = Admins.query.filter_by(username=username).first()
        if user:
            if user.is_active == False:
                flash("Your account has been deactivated !", "danger")
                return redirect(url_for("login.show") + "?error=inactive-user")

            if check_password_hash(user.password, password):
                login_user(user)
                user.last_logged_in_at = datetime.utcnow()
                db.session.commit()
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
