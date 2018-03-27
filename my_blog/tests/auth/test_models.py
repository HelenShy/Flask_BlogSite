from my_blog.blueprints.auth.models import User


class TestModel(object):
    """
    Class that contains models testing methods
    """
    def test_user(self):
        """
        Test that password getter is non-accessible
        :return: True if password getter is non-accessible
        """
        user = User(id=1, username='Test', email='test@mail.ru', password_hash='password')
        try:
            x = user.password
            assert False
        except AttributeError:
            assert True
