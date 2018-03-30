from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix
from flask_login import LoginManager
# from flask_talisman import Talisman
from flask_debugtoolbar import DebugToolbarExtension

from flask_uploads import UploadSet, configure_uploads, IMAGES
# from my_blog.blueprints.auth.models import User

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"

toolbar = DebugToolbarExtension()


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True,
                static_url_path='', static_folder='static')
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object('config.settings')
    db.init_app(app)
    login_manager.init_app(app)
    toolbar.init_app(app)
    # Talisman(app)

    if settings_override:
        app.config.update(settings_override)

    from my_blog.blueprints.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from my_blog.blueprints.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from my_blog.blueprints.blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint, url_prefix='/blog')

    from my_blog.blueprints.social_profile import profile_fb
    app.register_blueprint(profile_fb, url_prefix='/profile')

    from my_blog.blueprints.social_profile import profile_google
    app.register_blueprint(profile_google, url_prefix='/profile')

    from my_blog.blueprints.social_profile import profile_github
    app.register_blueprint(profile_github, url_prefix='/profile')

    from my_blog.blueprints.social_profile import profile
    app.register_blueprint(profile, url_prefix='/profile')

    from my_blog.blueprints.admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    app.config['UPLOADED_IMAGES_DEST'] = '/var/uploads'
    images = UploadSet('images', IMAGES)
    configure_uploads(app, (images,))

    return app


from my_blog.blueprints.auth.models import User


@login_manager.user_loader
def load_user(user_id):
    """
    Returns user by his id
    :param user_id: User id
    :return: User
    """
    u = User.query.get(user_id)
    return u
