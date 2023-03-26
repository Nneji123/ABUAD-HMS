import os

import sqlalchemy

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_admin import Admin
from webui import WebUI


from configurations.config import configs
from configurations.extensions import db, email, login_manager, socketio

from views.home import home
from views.index import index
from views.login import login
from views.logout import logout, CustomIndexView
from configurations.schema import Admins, AdminsView, db


load_dotenv()


def create_app(app):
    app.config.update(configs)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    login_manager.init_app(app)
    db.init_app(app)
    email.init_app(app)
    socketio.init_app(app)
    create_admin_views(app)
    app.app_context().push()
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(index)
    app.register_blueprint(login)
    app.register_blueprint(home)
    app.register_blueprint(logout)
    return None


def create_admin_views(app):
    admin = Admin(
        app, name="ABUAD", template_mode="bootstrap4", index_view=CustomIndexView()
    )
    admin.add_view(AdminsView(Admins, db.session))
    return admin


@login_manager.user_loader
def load_user(user_id):
    try:
        return Admins.query.get(int(user_id))
    except sqlalchemy.exc.OperationalError as e:
        return render_template("error.html", e="Database not found")


app = Flask(__name__)
app = create_app(app)
ui = WebUI(app, port=3000, debug=True, icon_path="logo.ico", app_name="ABUAD HMS")


if __name__ == "__main__":
    if not os.path.exists("var"):
        exec(open("init.py").read())
    else:
        pass
    # ui.run()
    app.run(host="0.0.0.0", port=3000, debug=True)
