from flask import url_for
from my_blog.tests.test_fixture import ViewTestMixin, \
    assert_status_with_message


class TestPage(object):
    def test_blog_read_page(self, client):
        """
        Test that read blog article response is 200
        """
        response = client.get(
            url_for('blog.read',
                    post_url='To-selfdoubting-developers-are-you-good-enough'))
        assert response.status_code == 200


class TestAuthorized(ViewTestMixin):
    def test_blog_add_blogpost(self):
        """
        Test that add post page response is 200
        """
        self.login()
        blogpost = {'title': 'test', 'content': 'testing...',
                    'published': True, 'imagePath': 'test_path',
                    'tags': 'one,two'}

        response = self.client.post(
            url_for('blog.add'), data=blogpost, follow_redirects=True)
        assert_status_with_message(200, response, 'New post to blog was added')

    def test_blog_edit_blogpost(self):
        """
        Test that edit post page response is 200
        """
        self.login()
        blogpost = {'title': 'test', 'content': 'testing...',
                    'published': True, 'imagePath': 'test_path',
                    'tags': ''}

        response = self.client.post(
            url_for('blog.edit', post_id=6), data=blogpost,
            follow_redirects=True)
        assert_status_with_message(
            200, response, 'Changes to blog post are stored')

    def test_blog_delete_blogpost_get_message(self):
        """
        Test that when post is asked to be deleted warning message shows
        """
        self.login()
        response = self.client.get(
            url_for('blog.delete', post_id=7), follow_redirects=True)
        assert_status_with_message(
            200, response, 'Please confirm deleting the post.')

    def test_blog_delete_blogpost(self):
        """
        Test that delete page response is 200
        """
        self.login()
        response = self.client.post(
            url_for('blog.delete', post_id=7), follow_redirects=True)
        assert response.status_code == 200

    def test_blog_delete_blogpost_404(self):
        """
        Test that on delete not existing page
        404 event handling page is shown
        """
        self.login()
        response = self.client.get(
            url_for('blog.delete', post_id=1000), follow_redirects=True)
        assert response.status_code == 404

    def test_blog_post_comment(self):
        """
        Test that on comment addition response is 200
        """
        self.login()
        comment = {'sender': 'test', 'content': 'testing...'}
        response = self.client.post(url_for(
            'blog.read',
            post_url='To-selfdoubting-developers-are-you-good-enough'),
            data=comment, follow_redirects=True)
        assert_status_with_message(
            200, response, 'New comment was added successfully')
