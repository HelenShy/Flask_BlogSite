from flask import Blueprint, render_template, flash, redirect,  url_for, abort
from .models import BlogPost
from datetime import datetime
from my_blog.app import db
from .forms import BlogPostForm

blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/<post_title>')
def read(post_title):
    """
    Generate page with selected blog post to read
    """
    title = post_title.replace('%20', ' ')
    blogpost = BlogPost.query.filter_by(title=title).first_or_404()
    return render_template('read.html', blogpost = blogpost)


@blog.route('/add', methods=['GET', 'POST'])
def add():
    """
    Generate page where new post for blog can be created
    """
    form = BlogPostForm()
    if form.validate_on_submit():
        title = form.title.data
        # if (form.published.data):
        date = datetime.utcnow()
        content = form.content.data
        imagePath = form.imagePath.data
        # published = form.published.data
        new_post = BlogPost(title = title, date = date, content = content, imagePath = imagePath)
        db.session.add(new_post)
        db.session.commit()
        flash("New post to blog was added")
        return redirect(url_for('admin.adminhome'))
    return render_template('edit.html', form = form, form_title = 'Add a new blog post')


@blog.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    """
    Generate page where selected post can be edited
    """
    blogpost = BlogPost.query.get_or_404(post_id)
    return render_template('edit.html', blogpost = blogpost)


@blog.route('/delete/<int:post_id>', methods=['GET', 'POST'])
def delete(post_id):
    """
    Generate page where selected post can be edited
    """
    blogpost = BlogPost.query.get_or_404(post_id)
    return render_template('delete.html', blogpost = blogpost)
