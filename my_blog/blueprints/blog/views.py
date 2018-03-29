from flask import Blueprint, render_template, flash, redirect,  \
    url_for, request, session
from flask_login import login_required
from datetime import datetime
import json
import os
from werkzeug.utils import secure_filename
import shutil

from .models import BlogPost, Comment
from my_blog.app import db
from .forms import BlogPostForm, CommentForm
from my_blog.blueprints.social_profile.models import UserProfile


blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/<post_url>', methods=['GET', 'POST'])
def read(post_url):
    """
    Generate page with selected blog post to read
    """
    blogpost = BlogPost.get_by_url(post_url)
    form = CommentForm()
    if 'current_profile' in session:
        user_profile = json.loads(session['current_profile'],
                                  object_hook=UserProfile.deserialize)
        form.sender.data = user_profile.name
        picture_url = user_profile.picture_url
        oauth_provider = user_profile.oauth_provider
    else:
        picture_url = ''
        oauth_provider = ''
    if request.method == 'POST':
        if form.validate_on_submit():
            sender = form.sender.data
            date = datetime.utcnow()
            content = form.content.data
            blogpost_id = blogpost.id
            level = 1
            new_comment = Comment(sender=sender,
                                  picture_url=picture_url,
                                  date=date,
                                  content=content,
                                  blogpost_id=blogpost_id,
                                  level=level)
            db.session.add(new_comment)
            db.session.commit()
            flash("New comment was added successfully")
            return redirect(url_for('blog.read', post_url=post_url))
    return render_template('read.html',
                           form=form,
                           blogpost=blogpost,
                           picture_url=picture_url,
                           oauth_provider=oauth_provider)


@blog.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    """
    Generate page where new post for blog can be created
    """
    form = BlogPostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            date = datetime.utcnow()
            content = form.content.data
            imagePath = form.imagePath.data
            published = form.published.data
            tags = form.tags.data
            new_post = BlogPost(title=title,
                                date=date,
                                content=content,
                                published=published,
                                tags=tags,
                                imagePath=imagePath)
            db.session.add(new_post)
            db.session.commit()
            post_id = BlogPost.get_by_title(title).id
            directory = os.path.join(img_dir, str(post_id))
            files_save(request.files.getlist('images_save'), directory)
            flash("New post to blog was added")
            return redirect(url_for('main.index'))
    return render_template('edit_form.html',
                           form=form,
                           form_title='Add a new blog post',
                           files=[])


basedir = os.path.abspath("./")
img_dir = os.path.join(basedir, 'my_blog', 'static', 'img')


@blog.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    """
    Generate page where selected post can be edited
    """
    blogpost = BlogPost.query.get(post_id)
    directory = os.path.join(img_dir, str(post_id))
    files_list = []
    if os.path.exists(directory):
        for root, dirs, files in os.walk(directory, topdown=False):
            for filename in files:
                files_list.append(filename)
    form = BlogPostForm(obj=blogpost)
    if request.method == 'POST':
        form.title.data = request.form['title']
        form.imagePath.data = request.form['imagePath']
        form.content.data = request.form['content']
        form.published.data = request.form.get('checkbox')
        form.tags.data = request.form['tags']
        files_to_delete = request.form.getlist('images_delete')
        if form.validate_on_submit():
            form.populate_obj(blogpost)
            db.session.commit()
            files_delete(request.form.getlist('images_delete'), directory)
            files_save(request.files.getlist('images_save'), directory)
            flash("Changes to blog post are stored")
            return redirect(url_for('blog.read',
                                    post_url=blogpost.url))
    return render_template('edit_form.html',
                           post_id=str(post_id),
                           form=form,
                           form_title='Edit blog post',
                           files=files_list)


@blog.route('/delete/<int:post_id>', methods=['GET', 'POST'])
@login_required
def delete(post_id):
    """
    Generate page where selected post can be edited
    """
    blogpost = BlogPost.query.get_or_404(post_id)
    if request.method == "POST":
        db.session.delete(blogpost)
        db.session.commit()
        img_directory = os.path.join(img_dir, str(post_id))
        if os.path.exists(img_directory):
            shutil.rmtree(img_directory, ignore_errors=True)
        flash("Post was deleted.")
        return redirect(url_for('main.index'))
    else:
        flash("Please confirm deleting the post.")
    return redirect(url_for('main.index'))


def files_save(files_list, directory):
    if len(files_list) > 0:
        for f in files_list:
            filename = secure_filename(f.filename)
            if not os.path.exists(directory):
                os.makedirs(directory)
            for root, dirs, files in os.walk(directory, topdown=False):
                if f not in files:
                    f.save(os.path.join(directory, filename))


def files_delete(files_list, directory):
    if len(files_list) > 0:
        if os.path.exists(directory):
            for filename in files_list:
                os.remove(os.path.join(directory, filename))
