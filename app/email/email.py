from flask_mail import Message
from app import mail, app
from config import Config


def sendMail(subject, email, content):
    message = Message(subject, sender = app.config['MAIL_USERNAME'], recipients = [email])
    message.body = content
    mail.send(message)
    return True

