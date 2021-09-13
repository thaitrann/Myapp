import hashlib
from flask import Flask, render_template, redirect, flash, url_for
from app import app
from .register_forms import RegisterForm


@app.route('/register', methods = ["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit() and form.password.data == form.confirm_password.data:
        flash('Yeu cau dang ki tu email: {}'.format(form.email.data))
        return redirect(url_for('register'))

    return render_template('register.html', title = 'Register', form = form)
        

   