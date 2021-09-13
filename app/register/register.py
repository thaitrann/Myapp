from wtforms.validators import Email
from app.models.user import User
import hashlib
from flask import Flask, render_template, redirect, flash, url_for
from app import app
from .register_forms import RegisterForm
from flask_login import current_user
from app import db

@app.route('/register', methods = ["GET","POST"])
def register():
    form = RegisterForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():
        user = User(email = form.email.data)
        user.setPassword(form.password.data)
        db.session.add(user)
        db.session.commit()
        
        flash('You are now registered user')
        return redirect(url_for('login'))

    return render_template('register.html', title = 'Register', form = form)
        

   