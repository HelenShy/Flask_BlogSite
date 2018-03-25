from flask import url_for


class TestMain():
    def test_main_page(self, client):
        """
        Test that main page response is 200
        """
        response = client.get(url_for('home'))
        assert response.status_code == 200
