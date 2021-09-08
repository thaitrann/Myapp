from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), validators.Email()])

    password = PasswordField('Password', validators=[
        DataRequired(),
        validators.EqualTo('confirm_password',  message = 'Password must match!')
    ])

    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        validators.EqualTo('password',  message = 'Password must match!')
    ])

    register = SubmitField('Register')