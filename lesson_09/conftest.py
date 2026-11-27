import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Импортируем Base, чтобы SQLAlchemy знала о таблицах
from models import Base  

DB_USER = "postgres"
DB_PASSWORD = "123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "mydatabase"

# Собираем строку подключения из переменных выше
DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


@pytest.fixture(scope="session")
def engine():
    # Создаем движок для подключения к базе
    eng = create_engine(DATABASE_URL)

    # Создаем таблицы в базе, если их там еще нет
    Base.metadata.create_all(eng)

    return eng


@pytest.fixture(scope="function")
def session(engine):
    # Создаем фабрику сессий, привязанную к нашему движку
    session_factory = sessionmaker(bind=engine)
    sess = session_factory()
    try:
        yield sess
    finally:
        # Откатываем транзакцию и закрываем сессию после теста
        try:
            sess.rollback()
        except Exception:
            pass
        sess.close()
        