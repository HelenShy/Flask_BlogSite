import pytest
from werkzeug.security import generate_password_hash

import os
from my_blog.app import create_app, db as _db
from my_blog.blueprints.auth.models import User


@pytest.yield_fixture(scope="session")
def app():
    """
    Setup flask test application

    :return: Flask app
    """
    basedir = os.path.abspath("./")
    db_uri = 'sqlite:///' + os.path.join(basedir, 'my_blog_test.db')
    params = {
        'DEBUG': False,
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': db_uri,
        'SERVER_NAME': 'localhost:8000',
        'WTF_CSRF_ENABLED': False,
        'WTF_CSRF_METHODS': []
    }

    _app = create_app(settings_override=params)

    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope="function")
def client(app):
    """
    Setup an app client
    :param app: Pytest yield_fixture
    :return: Flask app client
    """
    yield app.test_client()


@pytest.fixture(scope='session')
def db(app):
    """
    Setup our database, this only gets executed once per session.

    :param app: Pytest fixture
    :return: SQLAlchemy database session
    """
    # Create a single user because a lot of tests do not mutate this user.
    # It will result in faster tests.
    # _db.drop_all()
    # _db.create_all()

    password_hash = '12345'
    params = {
        'id': 2,
        'username': 'test',
        'password': password_hash,
        'email': 'test@mail.com'
    }

    admin = User(**params)

    # _db.session.add(admin)
    # _db.session.commit()

    return _db


@pytest.yield_fixture(scope='function')
def session(db):
    """
    Allow very fast tests by using rollbacks and nested sessions. This does
    require that your database supports SQL savepoints, and Postgres does.

    Read more about this at:
    http://stackoverflow.com/a/26624146

    :param db: Pytest fixture
    :return: None
    """
    db.session.begin_nested()

    yield db.session

    db.session.rollback()
