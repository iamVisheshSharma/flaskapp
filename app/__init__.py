from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
  app = Flask(__name__)
  # app.config.from_object(Config)
  app.config['SECRET_KEY'] =  '58022c2a91077bb30a3f83d0569c6562'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['MAIL_SERVER'] = 'smtp.mailtrap.io' #'smtp.googlemail.com'
  app.config['MAIL_PORT'] = 2525
  app.config['MAIL_USE_TLS'] = True
  app.config['MAIL_USERNAME'] = '824c9a7e44a2a7'
  app.config['MAIL_PASSWORD'] = 'eec6669b5b3833'

  db.init_app(app)
  bcrypt.init_app(app)
  login_manager.init_app(app)
  mail.init_app(app)

  from app.users.routes import users
  from app.posts.routes import posts
  from app.main.routes import main
  from app.errors.handler import errors

  app.register_blueprint(users)
  app.register_blueprint(posts)
  app.register_blueprint(main)
  app.register_blueprint(errors)

  return app
