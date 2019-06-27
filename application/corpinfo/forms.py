from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, ValidationError
from wtforms.validators import DataRequired, Optional, Length

from ..models import CorpInfo


class EditCorpInfo(FlaskForm):
    name = StringField('公司名', validators=[DataRequired()])
    biography = StringField('公司简介', validators=[DataRequired()])
    address = StringField('公司地址', validators=[DataRequired()])
    email = StringField('公司邮箱', validators=[DataRequired()])
    tel = StringField('联系电话', validators=[DataRequired()])


class AddCorpInfo(FlaskForm):
    name = StringField('公司名', validators=[DataRequired()])
    biography = StringField('公司简介', validators=[DataRequired()])
    address = StringField('公司地址', validators=[DataRequired()])
    email = StringField('公司邮箱', validators=[DataRequired()])
    tel = StringField('联系电话', validators=[DataRequired()])

    def validate_name(form, field):
        corpinfos = CorpInfo.get_or_none(CorpInfo.name == field.data)
        if corpinfos is not None:
            raise ValidationError('用户名已经被使用')

