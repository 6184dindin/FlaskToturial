from src.extensions import db
from src.models import BooksSchema, Books
from flask import request, jsonify
import json

book_schema = BooksSchema()
books_schema = BooksSchema(many=True)


def add_book_service():
    data = request.json
    if (
        data
        and "name" in data
        and "page_count" in data
        and "author_id" in data
        and "category_id" in data
    ):
        try:
            new_book = Books(
                data["name"], data["page_count"], data["author_id"], data["category_id"]
            )
            db.session.add(new_book)
            db.session.commit()
            return jsonify({"message": "Book added successfully"}), 201
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Error adding book"}), 400
    else:
        return jsonify({"message": "Invalid data"}), 400


def get_all_books_service():
    all_books = Books.query.all()
    if all_books:
        return books_schema.jsonify(all_books)
    else:
        return jsonify({"message": "No books found"}), 404


def get_book_by_id_service(book_id):
    book = Books.query.get(book_id)
    if book:
        return book_schema.jsonify(book)
    else:
        return jsonify({"message": "No book found"}), 404


def update_book_service(book_id):
    book = Books.query.get(book_id)
    if book:
        data = request.json
        if data:
            try:
                if "name" in data:
                    book.name = data["name"]
                if "page_count" in data:
                    book.page_count = data["page_count"]
                if "author_id" in data:
                    book.author_id = data["author_id"]
                if "category_id" in data:
                    book.category_id = data["category_id"]
                db.session.commit()
                return jsonify({"message": "Book updated successfully"}), 200
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Error updating book"}), 400
        else:
            return jsonify({"message": "Invalid data"}), 400
    else:
        return jsonify({"message": "No book found"}), 404


def delete_book_service(book_id):
    book = Books.query.get(book_id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return jsonify({"message": "Book deleted successfully"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Error deleting book"}), 400
    else:
        return jsonify({"message": "No book found"}), 404
