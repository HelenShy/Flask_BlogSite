from flask import url_for
from my_blog.tests.test_fixture import ViewTestMixin


class TestAuthorized(ViewTestMixin):
    def test_blogposts_panel(self):
        """
        Test that admin page with opened blogposts_panel response is 200
        """
        self.login()
        response = self.client.get(url_for('admin.blogposts_panel'))
        assert response.status_code == 200

    def test_comments_panel(self):
        """
        Test that admin page with opened comments_panel response is 200
        """
        self.login()
        response = self.client.get(url_for('admin.comments_panel'))
        assert response.status_code == 200