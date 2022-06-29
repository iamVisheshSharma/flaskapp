import os

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') 
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  MAIL_SERVER = 'smtp.mailtrap.io' #'smtp.googlemail.com'
  MAIL_PORT = 2525
  MAIL_USE_TLS = True
  MAIL_USERNAME = '824c9a7e44a2a7'
  MAIL_PASSWORD = 'eec6669b5b3833'