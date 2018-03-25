import pytest

from my_blog.app import create_app


@pytest.yield_fixture(scope="session")
def app():
    """
    Setup flask test application

    :return: Flask app
    """
    params = {
        'DEBUG': False,
        'TESTING': True
    }

    _app = create_app(settings_override=params)

    ctx = _app.context()
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
