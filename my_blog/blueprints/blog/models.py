from sqlalchemy import desc
from flask import Markup
from markdown import markdown
import re
from sqlalchemy.orm.exc import NoResultFound

from my_blog.app import db

tags = db.Table('blogpost_tag',
                db.Column('tag_id', db.Integer,
                          db.ForeignKey('tag.id')),
                db.Column('blogpost_id', db.Integer,
                          db.ForeignKey('blog_post.id')))


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _title = db.Column(db.String(128))
    date = db.Column(db.DateTime)
    content = db.Column(db.String)
    imagePath = db.Column(db.String)
    published = db.Column(db.Boolean)
    url = db.Column(db.String(128))
    _tags = db.relationship('Tag',
                            secondary=tags,
                            lazy='joined',
                            backref=db.backref('BlogPost',
                                               lazy='dynamic'))
    comments = db.relationship('Comment',
                               backref='blogpost',
                               lazy='dynamic')

    def __repr__(self):
        return self.title

    @staticmethod
    def get_by_title(title):
        return BlogPost.query.filter_by(url=title).first()

    @staticmethod
    def get_by_id(post_id):
        return BlogPost.query.get(post_id)

    @staticmethod
    def get_all():
        return BlogPost.query.all()

    @staticmethod
    def published_blogposts_page(pagenum):
        blogposts = BlogPost.query\
            .filter_by(published=True)\
            .order_by(desc(BlogPost.id))\
            .paginate(pagenum, 2, error_out=False)
        return blogposts

    @staticmethod
    def blogposts_page(pagenum):
        blogposts = BlogPost.query\
            .order_by(desc(BlogPost.id))\
            .paginate(pagenum, 2, error_out=False)
        return blogposts

    def markup_content(self):
        return Markup(markdown(self.content))

    def intro_content(self):
        return self.markup_content()[:700]

    def formated_date(self):
        return "{0:%B %d, %Y}".format(self.date).upper()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, string):
        self._title = string
        self.url = (re.sub('[^0-9a-zA-Z ]+', '', string)).replace(' ', '-')

    @property
    def tags(self):
        return ",".join([tag.name for tag in self._tags])

    @tags.setter
    def tags(self, string):
        if string:
            self._tags = [Tag.get_or_create(tag)
                          for tag in string.split(',')]
        else:
            self._tags = []


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def blogposts(self, pagenum=1):
        return self.BlogPost.order_by(desc(BlogPost.id)).paginate(pagenum, 2, error_out=False)

    def blogposts_published(self, pagenum=1):
        return self.BlogPost.filter_by(published=True).order_by(desc(BlogPost.id)).paginate(pagenum, 2, error_out=False)

    @staticmethod
    def get_or_create(name):
        try:
            return Tag.query.filter_by(name=name).one()
        except NoResultFound:
            return Tag(name=name)

    @staticmethod
    def all():
        return Tag.query.all()

    def __repr__(self):
        return self.name


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(128))
    picture_url = db.Column(db.String(128))
    date = db.Column(db.DateTime)
    content = db.Column(db.String(516))
    blogpost_id = db.Column(db.Integer, db.ForeignKey('blog_post.id'),
                            nullable=False)
    level = db.Column(db.Integer)

    @staticmethod
    def get_all():
        return Comment.query.all()

    def get_blogpost(self):
        return BlogPost.get_by_id(self.blogpost_id)

    def markup_content(self):
        return Markup(markdown(self.content))

    def formated_date(self):
        return "{0:%d.%m.%Y  %I:%M%p}".format(self.date).upper()
