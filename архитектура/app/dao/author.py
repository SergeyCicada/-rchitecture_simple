"""Класс для работы с моделями
 Реализуем CRUD
 Без бизнес логики, вся бизнес логика находится в сервисах"""
from архитектура.app.dao.model.author import Author


class AuthorDAO:
    def __init__(self, session):
        self.session = session

    def create(self, data):
        author = Author(**data)

        self.session.add(author)
        self.session.commit()

        return author

    def get_one(self, aid):
        return self.session.query(Author).get(aid)

    def get_all(self):
        return self.session.query(Author).all()

    def update(self, author):

        self.session.add(author)
        self.session.commit()

        return author

    def delete(self, aid):
        author = self.get_one(aid)
        self.session.delete(author)
        self.session.commit()
