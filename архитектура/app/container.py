"""Контейнер - временное хранилище сервисов и дополнительных объектов для их инициализации"""
from архитектура.app.dao.author import AuthorDAO
from архитектура.app.dao.book import BookDAO
from архитектура.app.database import db
from архитектура.app.services.author import AuthorService
from архитектура.app.services.book import BookService

author_dao = AuthorDAO(db.session)
author_service = AuthorService(author_dao)

book_dao = BookDAO(db.session)
book_service = BookService(book_dao)
