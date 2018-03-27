from flask import url_for
from my_blog.tests.test_fixture import ViewTestMixin, assert_status_with_message


class TestAuthorized(ViewTestMixin):
    def test_login(self):
        """
        Test login is successfull.
        """
        response = self.login()
        assert response.status_code == 200

    def test_logout(self):
        """
        Test logout is successfull.
        """
        self.login()
        response = self.logout()
        assert_status_with_message(200, response, 'User logged out.')
