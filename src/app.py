import os
import sqlite3

import sqlalchemy

# from dotenv import load_dotenv
from flask import Flask, render_template, send_from_directory
from flask_login import LoginManager

# from webui import WebUI
from flaskwebgui import FlaskUI
from werkzeug.security import generate_password_hash

from home import home
from index import index
from login import login
from logout import logout
from register import register
from schema import Users, db

# load_dotenv()


app = Flask(__name__, static_folder="./templates/static")
# ui = WebUI(
#     app,
#     url="127.0.0.1",
#     port=3000,
#     debug=True,
#     using_win32=True,
#     icon_path="logo.ico",
#     app_name="SmokeDetector",
# )  # Add WebUI
ui = FlaskUI(
    app=app, server="flask", port=5000, fullscreen=True, width=800, height=600
)  # Add WebUI


# SQLITE = os.getenv("SQLITE")

app.config["SECRET_KEY"] = "secret"
app.config.from_object(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database.db"


login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)
app.app_context().push()

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(home)
app.register_blueprint(logout)


@login_manager.user_loader
def load_user(user_id):
    try:
        return Users.query.get(int(user_id))
    except (sqlalchemy.exc.OperationalError) as e:
        return render_template("error.html", e="Database not found")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "./templates/static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


def create_new_user(username, email, password):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    hashed_password = generate_password_hash(password, method="sha256")
    cur.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (username, email, hashed_password),
    )
    conn.commit()
    conn.close()
    print("Database Executed Successfully!")


def start():
    if not os.path.exists("./database.db"):
        db.create_all()
        create_new_user("test", "test@gmail.com", "password")
        create_new_user("test2", "test2@gmail.com", "password")
    else:
        print("Database Exists with Current Users")



if __name__ == "__main__":
    start()
    ui.run()
    # app.run(host="0.0.0.0", port=3000, debug=True)
