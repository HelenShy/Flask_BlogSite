from flask import Blueprint, render_template
from .models import BlogPost

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
@main.route('/index')
def index():
	"""
	Generate main web page
	"""
	return render_template('home.html', blogposts = BlogPost.blogposts_page(1), pagenum = 1)


@main.route('/page/<pagenum>')
def page(pagenum):
	"""
	Generate main web page
	"""
	return render_template('home.html', blogposts = BlogPost.blogposts_page(int(pagenum)), pagenum=pagenum)


@main.app_errorhandler(403)
def page_not_found(e):
    return render_template('404.html'), 403

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
