from flask import Flask
from flask_restx import Api
from архитектура_упрощенная.app.config import Config
from архитектура_упрощенная.app.database import db
from архитектура_упрощенная.app.models import Book, Author
from архитектура_упрощенная.app.views.authors import author_ns
from архитектура_упрощенная.app.views.books import book_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()  # CONTEXT FOR SQLALCHEMY

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(author_ns)
    api.add_namespace(book_ns)


def load_data():
    b1 = Book(id=1, name="Harry Potter", year=1992)
    b2 = Book(id=2, name="Le comte de Monte-Cristo", year=1854)

    a1 = Author(id=1, first_name="Joana", last_name="Rouling")
    a2 = Author(id=2, first_name="Alexsandr", last_name="Dumas")

    db.drop_all()
    db.create_all()
    db.session.add_all([a1, a2])
    db.session.add_all([b1, b2])
    db.session.commit()


if __name__ == "__main__":
    app_config = Config()
    app = create_app(app_config)

    configure_app(app)
    load_data()

    app.run()
