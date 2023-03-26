import sys

from flask import Blueprint, flash, redirect, url_for
from flask_admin import expose
from flask_login import login_required, logout_user

sys.path.append("..")

from configurations.schema import MyAdminIndexView

logout = Blueprint("logout", __name__)


@logout.route("/logout")
@login_required
def show():
    logout_user()
    flash("You have successfully logged out!", "success")
    return redirect(url_for("login.show") + "?success=logged-out")


class CustomIndexView(MyAdminIndexView):
    @expose("/logout")
    def logout(self):
        logout_user()
        return redirect(url_for("login.show"))
