from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, ValidationError

class AuthForm(FlaskForm):
    authentication = StringField('Authentication', validators=[DataRequired()])
    submit = SubmitField('Submit')