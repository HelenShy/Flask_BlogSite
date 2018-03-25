from flask import Blueprint, render_template
from flask_login import login_required

from my_blog.blueprints.blog.models import BlogPost, Comment

admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/')
@admin.route('/posts')
@login_required
def blogposts_panel():
    """
    Show admin page with posts panel
    """
    return render_template('admin-posts_panel.html',
                           blogposts=BlogPost.get_all(),
                           comments=Comment.get_all(),
                           blogposts_qty=len(BlogPost.get_all()),
                           comments_qty=len(Comment.get_all()))


@admin.route('/comments')
@login_required
def comments_panel():
    """
    Show admin page with comments panel
    """

    return render_template('admin-comments_panel.html',
                           blogposts=BlogPost.get_all(),
                           comments=Comment.get_all(),
                           blogposts_qty=len(BlogPost.get_all()),
                           comments_qty=len(Comment.get_all()))
