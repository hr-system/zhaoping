from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, ValidationError
from wtforms.validators import DataRequired, Optional, Length
from ..models import User


class EditUser(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    nickname = StringField('姓名', validators=[DataRequired()])
    gender = SelectField('性别', validators=[DataRequired()], choices=(('M', '男'), ('F', '女')))
    # role = SelectField('角色', validators=[DataRequired()], choices=(('teacher', '教师'), ('student', '学生')))


class AddUser(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = StringField('密码', validators=[DataRequired(), Length(6, 20, '密码长度在6~20之间')])
    nickname = StringField('姓名', validators=[Optional()])
    gender = StringField('性别', validators=[DataRequired()])
    role = StringField('角色', validators=[DataRequired()])

    def validate_username(form, field):
        user = User.get_or_none(User.username == field.data)
        if user is not None:
            raise ValidationError('用户名已经被使用')