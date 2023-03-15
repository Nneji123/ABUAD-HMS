import sys
from cx_Freeze import setup, Executable

if sys.platform == "win32":
    base = "Win32GUI"


# List of files and directories to include in the build
included_files = [
    ("templates", "templates"),
    ("models", "models"),
    ("deep_sort", "deep_sort"),
    ("app.py", "app.py"),
    ("config.py", "config.py"),
    (".env", ".env"),
    ("home.py", "home.py"),
    ("init.py", "init.py"),
    ("index.py", "index.py"),
    ("utils.py", "utils.py"),
    ("login.py", "login.py"),
    ("logout.py", "logout.py"),
    ("schema.py", "schema.py"),
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
        "flaskwebgui",
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
            base=base,
            targetName="ABUAD-HMS.exe",
            shortcutName="ABUAD-HMS",
            shortcutDir="ProgramMenuFolder",
        ),
    ],
)
