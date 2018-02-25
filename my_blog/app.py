from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    db.init_app(app)

    from my_blog.blueprints.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from my_blog.blueprints.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from my_blog.blueprints.blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint, url_prefix='/blog')

    return app
