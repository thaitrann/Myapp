from app.home.home import home
from flask import Flask, render_template, redirect, flash, request
from flask.helpers import url_for
from app import app
from .login_forms import LoginForm
from flask_login import current_user, login_user
from app.models.user import User
from werkzeug.urls import url_parse

@app.route('/login', methods = ["GET","POST"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is None or not user.checkPassword(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('login'))

        login_user(user, remember = form.remember_me.data)

        next_page = request.args.get('next')
        print(next_page)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)

    return render_template('login.html', title = 'Sign In', form = form)