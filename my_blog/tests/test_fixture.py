import pytest
from flask import url_for
from werkzeug.security import generate_password_hash


def assert_status_with_message(status_code=200, response=None, message=None):
    """
    Check to see if a message is contained within a response.

    :param status_code: Status code that defaults to 200
    :type status_code: int
    :param response: Flask response
    :type response: str
    :param message: String to check for
    :type message: str
    :return: None
    """
    assert response.status_code == status_code
    assert message in str(response.data)


class ViewTestMixin(object):
    """
    Automatically load in a session and client, this is common for a lot of
    tests that work with views.
    """

    @pytest.fixture(autouse=True)
    def set_common_fixtures(self, session, client):
        self.session = session
        self.client = client

    def login(self, username='test', password='12345'):
        """
        Login a specific user.

        :return: Flask response
        """
        return login(self.client, username, password)

    def logout(self):
        """
        Logout a specific user.

        :return: Flask response
        """
        return logout(self.client)


def login(client, username='', password=''):
    """
    Log a specific user in.

    :param client: Flask client
    :param username: The username
    :param password: The password
    :return: Flask response
    """
    user = dict(userName=username, password=password)

    return client.post(url_for('auth.login'), data=user,
                       follow_redirects=True)


def logout(client):
    """
    Log a specific user out.

    :param client: Flask client
    :return: Flask response
    """
    return client.get(url_for('auth.logout'), follow_redirects=True)
