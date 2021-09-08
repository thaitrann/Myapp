from flask import Flask, render_template, redirect
from app import app

@app.route('/')
def index():
    return render_template('base.html')