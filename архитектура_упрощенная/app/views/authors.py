from flask import request
from flask_restx import Resource, Namespace

from архитектура_упрощенная.app.database import db
from архитектура_упрощенная.app.models import AuthorSchema, Author

author_ns = Namespace("authors")

author_schema = AuthorSchema()  # Сериализация одного объекта
authors_schema = AuthorSchema(many=True)  # Сериализация списка объектов


@author_ns.route('/')
class AuthorsView(Resource):
    def get(self):
        all_authors = db.session.query(Author).all()
        return author_schema.dump(all_authors), 200

    def post(self):
        req_json = request.json
        new_author = Author(**req_json)

        db.session.add(new_author)

        return "", 201


@author_ns.route('/<int:uid>')
class AuthorView(Resource):
    def get(self, uid: int):
        try:
            book = db.session.query(Author).filter(Author.id == uid).one()
            return author_schema.dump(book), 200
        except Exception:
            return "", 404

    def put(self, uid: int):
        author = db.session.query(Author).get(uid)
        req_json = request.json

        author.first_name = req_json.get("first_name")
        author.last_name = req_json.get("last_name")

        db.session.add(author)
        db.session.commit()

        return "", 204

    def patch(self, uid: int):
        author = db.session.query(Author).get(uid)
        req_json = request.json

        if "first_name" in req_json:
            author.name = req_json.get("first_name")
        if "last_year" in req_json:
            author.year = req_json.get("last_year")

        db.session.add(author)
        db.session.commit()

        return "", 204

    def delete(self, uid: int):
        author = db.session.query(Author).get(uid)

        db.session.delete(author)
        db.session.commit()

        return "", 204

