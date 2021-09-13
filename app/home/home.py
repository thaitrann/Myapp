from flask import Flask, render_template, redirect
from flask.helpers import url_for
from flask_login.utils import login_required
from app import app
from flask_login import logout_user


@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))