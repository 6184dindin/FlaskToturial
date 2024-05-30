from flask import request
from flask_restful import Resource
from ..models import *

borrowing_schema = BorrowingSchema()
borrowings_schema = BorrowingSchema(many=True)

class BookWithBorrowingStudents(Resource):
    def get(self, book_id):
        book = Books.query.get_or_404(book_id)
        borrowing_students = [student.name for student in book.students]
        return {'book': book.name, 'borrowing_students': borrowing_students}
    
    def post(self, book_id):
        student_id = request.json['student_id']

        new_borrowing = Borrowing(student_id=student_id, book_id=book_id)

        db.session.add(new_borrowing)
        db.session.commit()

        return borrowing_schema.jsonify(new_borrowing), 201