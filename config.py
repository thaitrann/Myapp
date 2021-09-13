import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'khong-doan-noi-dau'

    #mysql
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3306/myapp_db'

    #sqlserver
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://@THAITRAN\\SQLEXPRESS/myapp_db?trusted_connection=yes&driver=SQL Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'testflaskmail005@gmail.com'
    MAIL_PASSWORD = 'aA!123456'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

#Set-ExecutionPolicy Unrestricted -Scope Process 
#myenv\Scripts\activate