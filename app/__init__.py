from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from celery import Celery

load_dotenv()

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
RESULT_BACKEND = os.getenv('RESULT_BACKEND')


celery = Celery(__name__, broker=CELERY_BROKER_URL,
    result_backend=RESULT_BACKEND) 

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    celery.conf.update(app.config)

    db.init_app(app)
 
    migrate.init_app(app, db)

    with app.app_context():
        from .views.routes import route
        app.register_blueprint(route)
       
    return app


