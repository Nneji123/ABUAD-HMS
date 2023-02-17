import sys
from cx_Freeze import setup, Executable

if sys.platform == 'win32':
    base = 'Win32GUI'
    print("Windows")


# List of files and directories to include in the build
included_files = [
    ("templates", "templates"),
    ("models", "models"),
    ("deep_sort", "deep_sort"),
    ("frame", "frame"),
    ("app.py", "app.py"),
    ("home.py", "home.py"),
    ("index.py", "index.py"),
    ("login.py", "login.py"),
    ("logout.py", "logout.py"),
    ("register.py", "register.py"),
    ("schema.py", "schema.py"),
    ("logo.ico", "logo.ico"),
]

# Options for the build
build_options = {
    "packages": ["flask", "flask_login", "sqlalchemy","dotenv", "onnxruntime", "onnx", "flaskwebgui", "yolov5", "cv2", "numpy", "torch", "torchvision", "PIL", "tqdm", "requests", "matplotlib", "seaborn", "thop", "gdown"],
    "includes": ["werkzeug"],
    "excludes": ["tkinter", "pyside2"],
    "include_files": included_files,
}

# Setup function
setup(
    name="SmokeDetector",
    version="1.0",
    description="YOLOv5 Object Detection Flask App",
    options={"build_exe": build_options},
    executables=[Executable("app.py", icon="logo.ico")],
)