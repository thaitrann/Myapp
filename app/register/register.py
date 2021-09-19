from flask import jsonify
from wtforms.validators import Email
from app.models.user import User
from flask import Flask, render_template, redirect, flash, url_for, request
from app import app
from .register_forms import RegisterForm
from flask_login import current_user
from app import db
from app.email.email import sendMail, OTP
from app.email.email_forms import AuthForm


@app.route('/register', methods=["GET", "POST"])
def register():
    # content = 'test mail flask'
    # sendMail('test mail flask shell', email, content)
    form = RegisterForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.setPassword(form.password.data)
        json = jsonify(email=user.email, password=user.password_hash)
        return redirect(url_for('otp'))

        # db.session.add(user)
        # db.session.commit()

    return render_template('register.html', title='Register', form=form)
