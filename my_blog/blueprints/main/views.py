from flask import Blueprint, render_template, url_for

from my_blog.blueprints.blog.models import BlogPost, Tag
from .models import quote_list

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
@main.route('/index')
def index():
    """
    Generate main web page
    :return:
    """
    quote = quote_list.random_quote()
    return render_template('home.html', blogposts=BlogPost.blogposts_page(1), pagenum=1, tags=Tag.all(), quote=quote)


@main.route('/page/<pagenum>')
def page(pagenum):
    """
    Generate selected page of the blog archive
    :param pagenum:
    :return:
    """
    return render_template('home.html', blogposts=BlogPost.blogposts_page(int(pagenum)), pagenum=pagenum, tags=Tag.all())


@main.app_errorhandler(403)
def page_not_found(e):
    """
    Generate error pagenum
    :return: page with error 403
    """
    return render_template('403.html'), 403


@main.app_errorhandler(404)
def page_not_found(e):
    """
    Generate error pagenum
    :return: page with error 404
    """
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def server_error(e):
    """
    Generate error pagenum
    :return: page with error 500
    """
    return render_template('500.html'), 500
