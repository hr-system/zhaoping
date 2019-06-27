from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, ValidationError
from wtforms.validators import DataRequired, Optional, Email, Length
from ..models import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired('用户名不能为空')])
    password = StringField('密码', validators=[DataRequired('密码不能为空')])


class UserRegister(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    nickname = StringField('姓名', validators=[Optional()])
    password = StringField('密码', validators=[DataRequired(), Length(6, 20, '密码长度在6~20之间')])
    gender = StringField('性别', validators=[DataRequired('性别不能为空')])
    role = StringField('角色', validators=[DataRequired('请正确选择你的角色')])
    address=StringField('地址', validators=[DataRequired()])
    mail = StringField('Email', validators=[DataRequired('email不能为空'), Email('格式错误')])

    def validate_username(form, field):
        user = User.get_or_none(User.username == field.data)
        if user is not None:
            raise ValidationError('用户名已经被使用')


class AddPerson(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    name = StringField('姓名', validators=[Optional()])
    # gender = StringField('性别', validators=[Optional()])
    email = StringField('Email', validators=[DataRequired('email不能为空'), Email('格式错误')])

    def validate_username(form, field):
        user = User.get_or_none(User.username == field.data)
        if user is not None:
            raise ValidationError('用户名已经被使用')


class EditPerson(FlaskForm):
    nickname = StringField('姓名', validators=[DataRequired()])
    gender = SelectField(
                '性别',
                validators=[DataRequired()],
                choices=(('M', '男'), ('F', '女'))
            )
    address = StringField('地址', validators=[DataRequired()])
    mail = StringField('Email', validators=[DataRequired()])