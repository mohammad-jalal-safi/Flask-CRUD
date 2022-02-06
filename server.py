from flask import Flask, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import config as conf
from flask_login import LoginManager
from services.utils import main_bp
app = Flask(__name__)
db=SQLAlchemy(app)
login_manager = LoginManager()


def create_app():

    app.config['SECRET_KEY'] = conf.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = conf.DBURL
    login_manager.session_protection = "strong"
    login_manager.login_view = "login"
    login_manager.login_message_category = "info"
    login_manager.init_app(app)

    with app.app_context():
        # Register Blueprints
        app.register_blueprint(main_bp)
        db.create_all()

    return app

import services.login_services
from controllers.index_controller import *
from controllers.auth_controller import *
from controllers.profile_controller import *