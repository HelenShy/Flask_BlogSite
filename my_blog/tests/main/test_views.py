from flask import url_for
from my_blog.tests.test_fixture import ViewTestMixin


class TestPage(object):

    def test_index_page(self, client):
        """
        Test that index page response is 200
        """
        response = client.get(url_for('main.index'))
        assert response.status_code == 200

    def test_blog_page(self, client):
        """
        Test that blog page response is 200
        """
        response = client.get(url_for('main.page', pagenum=1))
        assert response.status_code == 200


class TestAuthorized(ViewTestMixin):
    def test_blog_page(self):
        """
        Test that index page response under authorised user is 200
        """
        self.login()
        response = self.client.get(url_for('main.page', pagenum=1))
        assert response.status_code == 200

    def test_index_page(self):
        """
        Test that blog page response under authorised user  is 200
        """
        self.login()
        response = self.client.get(url_for('main.index'))
        assert response.status_code == 200
