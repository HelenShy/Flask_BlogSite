from flask import url_for


class TestPage(object):
    def test_google_auth(self, client):
        """
        Test that google auth  page response is 200
        """
        response = client.get(url_for('google.connect_google'))
        assert response.status_code == 200

    def test_facebook_auth(self, client):
        """
        Test that facebook auth page response is 200
        """
        response = client.get(url_for('facebook.connect_facebook'))
        assert response.status_code == 200

    def test_github_auth(self, client):
        """
        Test that github auth page response is 200
        """
        response = client.get(url_for('github.connect_github'))
        assert response.status_code == 200

    def test_google_login(self, client):
        """
        Test that google auth page response is 200
        """
        response = client.get(url_for('profile.login', provider='google'))
        assert response.status_code == 200

    def test_facebook_login(self, client):
        """
        Test that facebook auth page response is 200
        """
        response = client.get(url_for('profile.login', provider='facebook'))
        assert response.status_code == 200

    def test_github_login(self, client):
        """
        Test that github auth page response is 200
        """
        response = client.get(url_for('profile.login', provider='github'))
        assert response.status_code == 200

    def test_profile_logout(self, client):
        """
        Test that facebook auth page response is 200
        """
        response = client.get(url_for('profile.logout'))
        assert response.status_code == 200
