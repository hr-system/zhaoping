from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, ValidationError
from wtforms.validators import DataRequired, Optional, Length

from ..models import RecruitInfo


class EditRecruitInfo(FlaskForm):
    name = StringField('公司名', validators=[DataRequired()])
    position = StringField('需求职位', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired()])
    tel = StringField('联系电话', validators=[DataRequired()])
    data = StringField('发布日期', validators=[DataRequired()])


class AddRecruitInfo(FlaskForm):
    name = StringField('公司名', validators=[DataRequired()])
    position = StringField('需求职位', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired()])
    tel = StringField('联系电话', validators=[DataRequired()])
    data = StringField('发布日期', validators=[DataRequired()])

    def validate_name(form, field):
        recruitinfos = RecruitInfo.get_or_none(RecruitInfo.name == field.data)
        if recruitinfos is not None:
            raise ValidationError('用户名已经被使用')

