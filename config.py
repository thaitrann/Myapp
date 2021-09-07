import os 

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MYSQL_HOST =  'localhost'
    MYSQL_USER =  'root'
    MYSQL_PASSWORD =  '1234'
    MYSQL_DB =  'excercise3'
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'testflaskmail005@gmail.com'
    MAIL_PASSWORD = 'aA!123456'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True