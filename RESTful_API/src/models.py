from .extensions import db, ma
from marshmallow import Schema, fields, post_dump

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

class StudentsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Students
        include_fk = True
        load_instance = True
        include_relationships = True

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

class AuthorsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Authors
        include_fk = True
        load_instance = True
        include_relationships = True

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

class CategoriesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Categories
        include_fk = True
        load_instance = True
        include_relationships = True

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    page_count = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    category = db.relationship('Categories', backref='books')

    def __init__(self, name, page_count, author_id, category_id):
        self.name = name
        self.page_count = page_count
        self.author_id = author_id
        self.category_id = category_id

class BooksSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Books
        include_fk = True
        load_instance = True
        include_relationships = True

    category = ma.Nested(CategoriesSchema) 

    @post_dump
    def merge_category(self, data, **kwargs):
        category_data = data.pop('category', {})
        for key, value in category_data.items():
            data[f'category_{key}'] = value
        return data

class Borrowing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    borrowing_date = db.Column(db.Date)
    returning_date = db.Column(db.Date)

    def __init__(self, student_id, book_id):
        self.student_id = student_id
        self.book_id = book_id

class BorrowingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Borrowing
        include_fk = True
        load_instance = True
        include_relationships = True
