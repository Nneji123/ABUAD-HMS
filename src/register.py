import sqlalchemy
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

from schema import Users, db

register = Blueprint("register", __name__, template_folder="./templates")
login_manager = LoginManager()
login_manager.init_app(register)


@register.route("/register", methods=["GET", "POST"])
def show():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        # confirm_password = request.form["confirm-password"]

        if username and email and password:
            if password:
                hashed_password = generate_password_hash(password, method="sha256")
                try:
                    new_user = Users(
                        username=username,
                        email=email,
                        password=hashed_password,
                    )

                    db.session.add(new_user)
                    db.session.commit()
                    flash("Account created successfully!", "success")
                except sqlalchemy.exc.IntegrityError:
                    flash("User already exists!", "failure")

                    return redirect(
                        url_for("register.show") + "?error=user-or-email-exists"
                    )
                return redirect(url_for("login.show") + "?success=account-created")
        else:
            flash("Please fill in all fields!", "failure")
            return redirect(url_for("register.show") + "?error=missing-fields")
    else:
        return render_template("register_and_login.html")
