from flask_mail import Message
from app import mail, app
from config import Config
from .email_forms import AuthForm
from flask import render_template, request


def sendMail(subject, email, content):
    message = Message(
        subject, sender=app.config['MAIL_USERNAME'], recipients=[email])
    message.body = content
    mail.send(message)
    return True

@app.route('/otp', methods = ["GET", "POST"])
def otp():
    if request.method == "POST":
        pass

    authform = AuthForm()
    return render_template('auth.html', title='Auth', authform=authform)

def OTP(json):
    return json
    
