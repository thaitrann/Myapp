from flask import Flask, render_template, redirect, flash
from flask.helpers import url_for
from app import app
from .login_forms import LoginForm

@app.route('/login', methods = ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Yeu cau dang nhap tu email: {}, remember_me: {}'.format(
            form.email.data, form.remember_me.data))
        return redirect(url_for('login'))

    return render_template('login.html', title='Sign In', form=form)