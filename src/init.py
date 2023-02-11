# import os
import sqlite3

from werkzeug.security import generate_password_hash

from app import db


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


def main():
    db.create_all()
    create_new_user("test", "test@gmail.com", "password")
    create_new_user("test2", "test2@gmail.com", "password")


if __name__ == "__main__":
    main()
