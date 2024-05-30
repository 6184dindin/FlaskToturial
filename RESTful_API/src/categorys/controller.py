from flask import request, Blueprint, jsonify
from ..extensions import db, ma
from src.models import CategoriesSchema, Categories


categories = Blueprint('categories', __name__)

@categories.route('/category', methods=['POST'])
def add_category():
    data = request.json
    if (
        data
        and "name" in data
    ):
        try:
            new_category = Categories(
                data["name"]
            )
            db.session.add(new_category)
            db.session.commit()
            return jsonify({"message": "category added successfully"}), 201
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Error adding category"}), 400
    else:
        return jsonify({"message": "Invalid data"}), 400
    
@categories.route('/categories', methods=['GET'])
def get_categories():
    try:
        categories = Categories.query.all()
        categories_list = [{"id": category.id, "name": category.name} for category in categories]
        return jsonify(categories_list), 200
    except Exception as e:
        return jsonify({"message": "Error retrieving categories", "error": str(e)}), 400