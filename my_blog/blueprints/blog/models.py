from my_blog.app import db
from sqlalchemy import desc
from flask import Markup
from markdown import markdown

tags = db.Table('blogpost_tag',
                db.Column('tag_id', db.Integer,
                          db.ForeignKey('tag.id')),
                db.Column('blogpost_id', db.Integer,
                          db.ForeignKey('blog_post.id')))


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    date = db.Column(db.DateTime)
    content = db.Column(db.String)
    imagePath = db.Column(db.String)
    published = db.Column(db.Boolean)
    _tags = db.relationship('Tag',
                            secondary=tags,
                            lazy='joined',
                            backref=db.backref('BlogPost',
                                               lazy='dynamic'))
    comments = db.relationship('Comment',
                               backref='blogpost',
                               lazy='dynamic')

    def __repr__(self):
        return "<User(title='{%s}', " \
               "date='{%s}', " \
               "content='{%s[:100]}', " \
               "imagePath ='{}')>".\
            format(self.title, self.date, self.content, self.imagePath)

    @staticmethod
    def get_by_title(title):
        title = title.replace('-', ' ')
        return BlogPost.query.filter_by(title=title).first()

    @staticmethod
    def get_by_id(post_id):
        return BlogPost.query.get(post_id)

    @staticmethod
    def get_all():
        return BlogPost.query.all()

    @staticmethod
    def blogposts_page(pagenum):
        blogposts = BlogPost.query\
            .filter_by(published=True)\
            .order_by(desc(BlogPost.id))\
            .paginate(pagenum, 2, error_out=False)
        return blogposts

    def title_url(self):
        return self.title.replace(' ', '-')

    def markup_content(self):
        return Markup(markdown(self.content))

    def intro_content(self):
        return self.markup_content()[:700]

    def formated_date(self):
        return "{0:%B %d, %Y}".format(self.date).upper()

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

    @property
    def blogposts(self):
        return self.BlogPost.paginate(1, 2, error_out=False)

    @staticmethod
    def get_or_create(name):
        return Tag.query.filter_by(name=name).one()

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
