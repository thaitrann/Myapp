from wtforms.validators import Email
from app.models.user import User
from flask import Flask, render_template, redirect, flash, url_for, request
from app import app
from .register_forms import RegisterForm
from flask_login import current_user
from app import db
from app.email.email import sendMail

@app.route('/register', methods = ["GET","POST"])
def register():
    form = RegisterForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():
        content = 'test mail flask'
        sendMail('test mail flask shell', form.email.data, content)

        user = User(email = form.email.data)
        user.setPassword(form.password.data)
        db.session.add(user)
        db.session.commit()
            
        flash('You are now registered user')
        return redirect(url_for('login'))

    return render_template('register.html', title = 'Register', form = form)
        

   