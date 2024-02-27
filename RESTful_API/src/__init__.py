from flask import Flask
from .books.controller import books
from .extensions import db, ma
from .models import Books, Authors, Categories, Borrowing, Students
import os

def create_db(app):
    if not os.path.exists('src/library.db'):
        with app.app_context():
            db.create_all()
            print('Database created')

def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)
    ma.init_app(app)
    create_db(app)

    app.register_blueprint(books)
    return app