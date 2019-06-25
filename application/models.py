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


class CorpSum(flask_db.Model):
    name = CharField()
    type = CharField()
    date = DateField()

    class Meta:
        database = flask_db.database


class CorpInfo(flask_db.Model):
    name = CharField()
    biography = CharField()
    address = CharField()
    email = CharField()
    tel = CharField()

    class Meta:
        database = flask_db.database


class RecruitInfo(flask_db.Model):
    name = CharField()
    position = CharField()
    type = CharField()
    email = CharField()
    tel = CharField()
    date = DateField()

    class Meta:
        database = flask_db.database


class CVInfo(flask_db.Model):
    name = CharField()
    gender = CharField()
    email = CharField()
    tel = CharField()
    address = CharField()
    birthday = DateField()

    class Meta:
        database = flask_db.database

