from flask import Blueprint, render_template
from flask_login import current_user

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
    if current_user.is_authenticated:
        blogposts = BlogPost.blogposts_page(1)
    else:
        blogposts = BlogPost.published_blogposts_page(1)
    return render_template('home.html', blogposts=blogposts, pagenum=1,
                           tags=Tag.all(), quote=quote, tag=None)


@main.route('/page/<pagenum>')
def page(pagenum):
    """
    Generate selected page of the blog archive
    :param pagenum:
    :return:
    """
    quote = quote_list.random_quote()
    if current_user.is_authenticated:
        blogposts = BlogPost.blogposts_page(int(pagenum))
    else:
        blogposts = BlogPost.published_blogposts_page(int(pagenum))
    return render_template('home.html', blogposts=blogposts, pagenum=pagenum, tags=Tag.all(), quote=quote, tag=None)


@main.route('/tag/<name>')
def tag(name):
    return tag_page(name, 1)


@main.route('/tag/<name>/<pagenum>')
def tag_page(name, pagenum):
    selected_tag = Tag.query.filter_by(name=name).first()
    quote = quote_list.random_quote()
    if current_user.is_authenticated:
        blogposts = selected_tag.blogposts(int(pagenum))
    else:
        blogposts = selected_tag.blogposts_published(int(pagenum))
    return render_template('tag.html', tag=selected_tag.name, tags=Tag.all(), quote=quote, blogposts=blogposts,
                           pagenum=pagenum)


@main.app_errorhandler(403)
def page_not_found_403(e):
    """
    Generate error pagenum
    :return: page with error 403
    """
    return render_template('403.html'), 403


@main.app_errorhandler(404)
def page_not_found_404(e):
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
