from flask import request
from flask_restful import Resource
from ..models import *


author_schema = AuthorsSchema()
authors_schema = AuthorsSchema(many=True)

class AuthorResource(Resource):
    def get(self, author_id):
        author = Authors.query.get_or_404(author_id)
        return author_schema.dump(author)
    
    def delete(self, author_id):
        author = Authors.query.get_or_404(author_id)
        db.session.delete(author)
        db.session.commit()
        return '', 204

class AuthorListResource(Resource):
    def get(self):
        authors = Authors.query.all()
        return authors_schema.dump(authors)
    
    def post(self):
        new_author = Authors(
            name=request.json['name']
        )
        db.session.add(new_author)
        db.session.commit()
        return author_schema.dump(new_author), 201