import os

import sqlalchemy

from dotenv import load_dotenv
from flask import Flask, render_template, send_from_directory
from flask_admin import Admin
from flask_login import LoginManager

from flaskwebgui import FlaskUI


from config import configs
from home import home
from index import index
from login import login
from logout import logout, CustomIndexView
from schema import Admins, AdminsView, db


load_dotenv()


app = Flask(__name__, static_folder="./templates/static")
ui = FlaskUI(
    app=app, server="flask", port=5000, fullscreen=True, width=800, height=600
)

SERVER_MODE = os.getenv("SERVER_MODE")
if SERVER_MODE in configs:
    app.config.update(configs[SERVER_MODE])
    app.config.from_object(__name__)
else:
    raise ValueError(f"Unknown server mode: {SERVER_MODE}")


login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)
app.app_context().push()

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(home)
app.register_blueprint(logout)

admin = Admin(
    app, name="ABUAD", template_mode="bootstrap4", index_view=CustomIndexView()
)
admin.add_view(AdminsView(Admins, db.session))


@login_manager.user_loader
def load_user(user_id):
    try:
        return Admins.query.get(int(user_id))
    except (sqlalchemy.exc.OperationalError) as e:
        return render_template("error.html", e="Database not found")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "./templates/static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    # ui.run()
    app.run(
        host="0.0.0.0", port=3000, debug=configs[SERVER_MODE]["DEBUG"], threaded=True
    )
