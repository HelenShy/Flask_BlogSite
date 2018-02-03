from flask import Flask, render_template


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        """
        Render a Hello World response.

        :return: Flask response
        """
        return render_template('base.html')

    return app
