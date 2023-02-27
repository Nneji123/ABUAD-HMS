from flask import Blueprint, flash, redirect, url_for
from flask_admin import expose
from flask_login import LoginManager, login_required, logout_user


from schema import MyAdminIndexView

logout = Blueprint("logout", __name__, template_folder="./frontend")
login_manager = LoginManager()
login_manager.init_app(logout)


@logout.route("/logout")
@login_required
def show():
    success = True
    logout_user()
    flash("You have successfully logged out!", "success")
    return redirect(url_for("login.show") + "?success=logged-out")

class CustomIndexView(MyAdminIndexView):
    @expose("/logout")
    def logout(self):
        logout_user()
        return redirect(url_for("login.show"))
