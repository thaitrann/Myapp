import hashlib
from flask import Flask, render_template, request, redirect
from app import *

@app.route('/', methods = ["GET","POST"])
def Register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        email = request.form['email']
        password = hashlib.sha512(request.form['password'].encode("utf-8")).hexdigest() 
        return password
    