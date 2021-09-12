from flask import Flask, render_template, redirect
from flask.helpers import url_for
from app import app
from flask_login import logout_user

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))