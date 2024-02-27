from flask import request, Blueprint
from .services import *

books = Blueprint('books', __name__)

@books.route('/book-management/add_book', methods=['POST'])
def add_book():
    return add_book_service()

@books.route('/book-management/books', methods=['GET'])
def get_all_books():
    return get_all_books_service()

@books.route('/book-management/book/<book_id>', methods=['GET'])
def get_book_by_id(book_id):
    return get_book_by_id_service(book_id)

@books.route('/book-management/book/<book_id>', methods=['PUT'])
def update_book(book_id):
    return update_book_service(book_id)

@books.route('/book-management/book/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    return delete_book_service(book_id)