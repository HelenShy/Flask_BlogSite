from flask import Flask, render_template

from my_blog.blueprints.main import main


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')

    app.register_blueprint(main)
    # @app.route('/', methods=['GET', 'POST'])
    # def index():
    #     """
    #     Render a Hello World response.
    #
    #     :return: Flask response
    #     """
    #     return render_template('base.html')

    return app
