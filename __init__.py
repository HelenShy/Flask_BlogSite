from flask import Flask, render_template


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    return app

app = create_app()
from . import views
