import sys
import shutil
import os
from cx_Freeze import setup, Executable

if sys.platform == "win32":
    base = "Win32GUI"


# List of files and directories to include in the build
included_files = [
    ("templates", "templates"),
    ("models", "models"),
    ("deep_sort", "deep_sort"),
    ("app.py", "app.py"),
    ("configurations", "configurations"),
    (".env", ".env"),
    ("views", "views"),
    ("init.py", "init.py"),
    ("static", "static"),
    ("logo.ico", "logo.ico"),
]

# Options for the build
build_options = {
    "packages": [
        "flask",
        "flask_login",
        "flask_mail",
        "flask_admin",
        "sqlalchemy",
        "dotenv",
        "onnxruntime",
        "onnx",
        "webui",
        "yolov5",
        "cv2",
        "numpy",
        "torch",
        "torchvision",
        "PIL",
        "tqdm",
        "requests",
        "matplotlib",
        "seaborn",
        "thop",
        "gdown",
    ],
    "includes": ["werkzeug", "sqlite3"],
    "excludes": ["tkinter"],
    "include_files": included_files,
}

# Setup function
setup(
    name="ABUAD-HMS",
    version="1.0",
    description="ABUAD Hostel Monitoring System Application",
    options={"build_exe": build_options},
    executables=[
        Executable(script="init.py"),
        Executable(
            script="app.py",
            icon="logo.ico",
            target_name="ABUAD-HMS.exe",
            shortcut_name="ABUAD-HMS",
            shortcut_dir="ProgramMenuFolder",
        ),
    ],
)


# Define the post build function
def post_build(build_dir):
    # Define the source and destination paths
    src_path = os.path.join("..", "env", "Lib", "site-packages", "matplotlib.libs")
    dest_path = os.path.join(build_dir, "lib")
    # Copy the matplotlib.libs folder to the build directory
    shutil.copytree(src_path, os.path.join(dest_path, "matplotlib.libs"))


post_build(r"build\exe.win-amd64-3.8")
