"""Сервисы - прокси сервер для взаимодействия с DAO
Вся бизнес логика находится здесь"""

from архитектура.app.dao.book import BookDAO


class BookService:
    def __init__(self, dao: BookDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        bid = data.get("id")
        book = self.get_one(bid)

        book.name = data.get("name")
        book.year = data.get("year")

        self.dao.update(book)

    def update_partial(self, data):  # из dao удалили этот метод, реализуем метод сервиса через update в DAO
        bid = data.get("id")
        book = self.get_one(bid)

        if "first_name" in data:
            book.name = data.get("name")
        if "last_name" in data:
            book.year = data.get("year")

        self.dao.update(book)

    def delete(self, bid):
        self.dao.delete(bid)
