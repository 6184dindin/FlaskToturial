from .extensions import db, ma

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    birth_date = db.Column(db.Date)
    gender = db.Column(db.String(10))
    class_name = db.Column(db.String(80))

    def __init__(self, name, email, birth_date, gender, class_name):
        self.name = name
        self.email = email
        self.birth_date = birth_date
        self.gender = gender
        self.class_name = class_name

class StudentsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'birth_date', 'gender', 'class_name')

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

class AuthorsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

class CategoriesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    page_count = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def __init__(self, name, page_count, author_id, category_id):
        self.name = name
        self.page_count = page_count
        self.author_id = author_id
        self.category_id = category_id

class BooksSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'page_count', 'author_id', 'category_id')

class Borrowing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    borrowing_date = db.Column(db.Date)
    returning_date = db.Column(db.Date)

    def __init__(self, student_id, book_id, borrowing_date, returning_date):
        self.student_id = student_id
        self.book_id = book_id
        self.borrowing_date = borrowing_date
        self.returning_date = returning_date

class BorrowingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'student_id', 'book_id', 'borrowing_date', 'returning_date')
