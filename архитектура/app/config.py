class Config:
    DEBUG = True
    SECRET = 'test'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Подключение к БД
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Отключение уведомлений
