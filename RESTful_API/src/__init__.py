from flask import Flask
from .books.controller import books
from .categorys.controller import categories
from .authors.controller import *
from .borrowing.controller import *
from .students.controller import *
from .extensions import db, ma
from .models import Books, Authors, Categories, Borrowing, Students
import os
from flask_restful import Api

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
    app.register_blueprint(categories)

    api = Api(app)
    api.add_resource(AuthorResource, '/authors/<int:author_id>')
    api.add_resource(AuthorListResource, '/authors')
    api.add_resource(BookWithBorrowingStudents,'/books/borrowing_students/<int:book_id>')

    api.add_resource(StudentResource, '/students', '/students/<int:student_id>')
    return app