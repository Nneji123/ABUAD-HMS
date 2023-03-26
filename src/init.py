import os

from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from app import db
from configurations.schema import Admins

load_dotenv()


def create_new_user(username, email, password):
    try:
        password_hash = generate_password_hash(password, method="sha256")
        new_user = Admins(username=username, email=email, password=password_hash)
        db.session.add(new_user)
        db.session.commit()
        print("Admin Created")
    except IntegrityError as e:
        db.session.rollback()
        print("Database not found")
        print(e)
    finally:
        db.session.close()


def main():
    if not os.path.exists("./database.db"):
        db.create_all()
        username = os.getenv("ADMIN_USERNAME")
        email = os.getenv("ADMIN_EMAIL")
        password = os.getenv("ADMIN_PASSWORD")
        create_new_user(username=username, email=email, password=password)
    else:
        print("Database Exists with Current Admins")


if __name__ == "__main__":
    main()
