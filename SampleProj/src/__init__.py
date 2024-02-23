from flask import Flask
import os
from dotenv import load_dotenv
from .user import user
from .views import views

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
DB_NAME = os.getenv('DB_NAME')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(user, url_prefix='/user')
    return app