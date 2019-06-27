from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, ValidationError
from wtforms.validators import DataRequired, Optional, Length
from application.models import CVInfo


class EditCVInfo(FlaskForm):
    name = StringField('姓名', validators=[DataRequired()])
    gender = StringField('性别', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired()])
    tel = StringField('电话', validators=[DataRequired()])
    address = StringField('地址', validators=[DataRequired()])
    birthday = StringField('出生日期', validators=[DataRequired()])


class AddCVInfo(FlaskForm):
    name = StringField('姓名', validators=[DataRequired()])
    gender = SelectField('性别', validators=[DataRequired()], choices=(('M', '男'), ('F', '女')))
    email = StringField('邮箱', validators=[DataRequired()])
    tel = StringField('电话', validators=[DataRequired()])
    address = StringField('地址', validators=[DataRequired()])
    birthday = StringField('出生日期', validators=[DataRequired()])

    def validate_name(form, field):
        cvinfos = CVInfo.get_or_none(CVInfo.name == field.data)
        if cvinfos is not None:
            raise ValidationError('用户名已经被使用')

