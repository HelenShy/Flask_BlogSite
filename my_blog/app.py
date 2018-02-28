from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_potection = "strong"
login_manager.login_view = "admin.login"


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    db.init_app(app)
    login_manager.init_app(app)

    from my_blog.blueprints.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from my_blog.blueprints.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from my_blog.blueprints.blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint, url_prefix='/blog')

    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    
    return app

from my_blog.blueprints.admin.models import User
@login_manager.user_loader
def load_user(id):
     # 1. Fetch against the database a user by `id`
     # 2. Create a new object of `User` class and return it.
     u = User.query.get(id)
     return u
