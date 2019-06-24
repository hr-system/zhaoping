from peewee import *
from flask_login import UserMixin

from .extensions import flask_db


class User(UserMixin, flask_db.Model):
    username = CharField(null=False, index=True, unique=True)
    nickname = CharField(null=False)
    password = CharField(null=False)
    gender = CharField(null=False, choices=(('M', '男'), ('F', '女')))
    address = CharField(null=True, max_length=500)
    mail = CharField(null=True, max_length=100)
    role = CharField(null=False, choices=(('teacher', '教师'), ('student', '学生')))

    class Meta:
        database = flask_db.database
