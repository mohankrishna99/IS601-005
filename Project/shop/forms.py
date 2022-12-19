from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, IntegerField, DecimalField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class ItemForm(FlaskForm):
    id = HiddenField("id", validators=[Optional()])
    name = StringField("name", validators=[DataRequired(), Length(max=30)])
    description = TextAreaField("description", validators=[DataRequired()])
    category = TextAreaField("category", validators=[DataRequired(), Length(max=30)])
    stock = IntegerField("stock", validators=[NumberRange(min=0)])
    unit_price = DecimalField("unit_price", validators=[NumberRange(min=0)])
    visibility = BooleanField("visibility")
    submit = SubmitField("Save")