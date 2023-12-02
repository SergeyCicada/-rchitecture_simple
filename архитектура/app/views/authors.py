from flask import request
from flask_restx import Resource, Namespace

from архитектура.app.container import author_service
from архитектура.app.dao.model.author import AuthorSchema

author_ns = Namespace("authors")

author_schema = AuthorSchema()  # Сериализация одного объекта
authors_schema = AuthorSchema(many=True)  # Сериализация списка объектов


@author_ns.route('/')
class AuthorsView(Resource):
    def get(self):
        all_authors = author_service.get_all()
        return authors_schema.dump(all_authors), 200

    def post(self):
        req_json = request.json
        author_service.create(req_json)

        return "", 201


@author_ns.route('/<int:uid>')
class AuthorView(Resource):
    def get(self, uid: int):
        try:
            book = author_service.get_one(uid)
            return author_schema.dump(book), 200
        except Exception:
            return "", 404

    def put(self, uid: int):
        req_json = request.json
        req_json["id"] = uid
        author_service.update(req_json)

        return "", 204

    def patch(self, uid: int):
        req_json = request.json
        req_json["id"] = uid
        author_service.update_partial(req_json)

        return "", 204

    def delete(self, uid: int):
        author_service.delete(uid)

        return "", 204

