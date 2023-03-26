import sys

from datetime import datetime

from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash

sys.path.append("..")

from .extensions import db


class Admins(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_logged_in_at = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, default=True)


class AdminsView(ModelView):
    column_searchable_list = ["username", "email", "created_at", "is_active"]
    column_filters = ["username"]
    column_exclude_list = ["password"]
    form_excluded_columns = ["id"]

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password, method="sha256")
        return super(AdminsView, self).on_model_change(form, model, is_created)


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_active
