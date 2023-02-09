import os

import sqlalchemy
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_login import LoginManager
from webui import WebUI

from index import index
from login import login
from logout import logout
from schema import Users, db
from register import register
from home import home

load_dotenv()


app = Flask(__name__, static_folder="./templates/static")
ui = WebUI(app, url="127.0.0.1", port=3000, debug=False, using_win32=True, icon_path="logo.ico", app_name="SmokeDetector" ) # Add WebUI
# ui = FlaskUI(app, width=800, height=600) # Add WebUI


SQLITE = os.getenv("SQLITE")

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = SQLITE


login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)
app.app_context().push()

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(home)



@login_manager.user_loader
def load_user(user_id):
    try:
        return Users.query.get(int(user_id))
    except (sqlalchemy.exc.OperationalError) as e:
        return render_template("error.html", e="Database not found")


if __name__ == "__main__":
    ui.run()
    # app.run(host="0.0.0.0", port=3000, debug=True)
