from flask import Blueprint, render_template, flash, redirect,  url_for, abort, request
from flask_login import login_required, current_user
from datetime import datetime

from .models import BlogPost
from my_blog.app import db
from .forms import BlogPostForm

blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/<post_title>')
def read(post_title):
    """
    Generate page with selected blog post to read
    """
    blogpost = BlogPost.get_by_title(post_title)
    return render_template('read.html', blogpost = blogpost)


@blog.route('/add', methods=['GET', 'POST'])
@login_required
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
        return redirect(url_for('main.index'))
    return render_template('edit.html', form = form, form_title = 'Add a new blog post')


@blog.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    """
    Generate page where selected post can be edited
    """
    blogpost = BlogPost.query.get(post_id)
    form = BlogPostForm(obj = blogpost)
    if request.method == 'POST':
        form.title = request.form['title']
        form.imagePath = request.form['imagePath']
        form.content = request.form['content']
        if form.validate_on_submit():
            form.populate_obj(blogpost)
            db.session.commit()
            flash("Changes to blog post are stored")
            return redirect(url_for('main.index'))
    return render_template('edit.html', form = form, form_title = 'Edit blog post')


@blog.route('/delete/<int:post_id>', methods=['GET', 'POST'])
@login_required
def delete(post_id):
    """
    Generate page where selected post can be edited
    """
    blogpost = BlogPost.query.get_or_404(post_id)
    if (request.method == "POST"):
        db.session.delete(blogpost)
        db.session.commit()
        flash("Deleted")
        return redirect(url_for('main.index', blogposts = BlogPost.blogposts_page(1), pagenum = 1, user="admin"))
    else:
        flash("Please confirm deleting the bookmark.")
    return  render_template('main.index', post_id=post_id)
