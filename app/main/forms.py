from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_wtf import FlaskForm

class NameForm(FlaskForm):
    name = StringField("What's your name?", validators=[Required()])
    submit = SubmitField('submit')