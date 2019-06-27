from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, ValidationError
from wtforms.validators import DataRequired, Optional, Length

from ..models import CorpSum


class EditCorpSum(FlaskForm):
    name = StringField('公司名', validators=[DataRequired()])
    type = StringField('类别', validators=[DataRequired()])
    data = StringField('日期', validators=[DataRequired()])


class AddCorpSum(FlaskForm):
    name = StringField('公司名', validators=[DataRequired()])
    type = StringField('类别', validators=[DataRequired()])
    data = StringField('日期', validators=[DataRequired()])

    def validate_name(form, field):
        corpsums = CorpSum.get_or_none(CorpSum.name == field.data)
        if corpsums is not None:
            raise ValidationError('用户名已经被使用')

