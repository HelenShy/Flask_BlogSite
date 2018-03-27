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
