"""Класс для работы с моделями
 Реализуем CRUD"""

from архитектура.app.dao.model.book import Book


class BookDAO:
    def __init__(self, session):
        self.session = session

    def create(self, data):
        book = Book(**data)

        self.session.add(book)
        self.session.commit()

        return book

    def get_one(self, bid):
        return self.session.query(Book).get(bid)

    def get_all(self):
        return self.session.query(Book).all()

    def update(self, data):
        aid = data.get("id")
        book = self.get_one(aid)

        book.name = data.get("name")
        book.year = data.get("year")

        self.session.add(book)
        self.session.commit()

        return book

    def delete(self, bid):
        book = self.get_one(bid)
        self.session.delete(book)
        self.session.commit()
