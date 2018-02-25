from flask import Blueprint, render_template
from my_blog.blueprints.blog.models import BlogPost

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/')
def adminhome():
	"""
	Generate main web page
	"""
	return render_template('admin.html', blogposts = BlogPost.blogposts_page(1), pagenum = 1, user="admin") #edit
