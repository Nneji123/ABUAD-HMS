"""Application Configurations"""

import os
from dotenv import load_dotenv

load_dotenv()


configs = {
"MAIL_SERVER": os.getenv("MAIL_SERVER"),
"MAIL_PORT": os.getenv("MAIL_PORT"),
"MAIL_USERNAME": os.getenv("MAIL_USERNAME"),
"MAIL_PASSWORD": os.getenv("MAIL_PASSWORD"),
"MAIL_USE_TLS": True,
"MAIL_USE_SSL": False,
"SECRET_KEY": os.getenv("SECRET_KEY"),
"SQLALCHEMY_DATABASE_URI": "sqlite:///./database.db",
"LOGIN_DISABLED": False,
"SQLALCHEMY_TRACK_MODIFICATIONS": False
}
