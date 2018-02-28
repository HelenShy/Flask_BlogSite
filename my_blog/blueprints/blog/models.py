from  my_blog.app import  db
from sqlalchemy import desc

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    date = db.Column(db.DateTime)
    content = db.Column(db.String)
    imagePath = db.Column(db.String)
    # published = db.Column(db.Boolean)
    # _tags = db.relationship('Tag', secondary ='tags', lazy ='joined', backref=db.backref('BlogPost', lazy='dynamic'))

    def __repr__(self):
        return "<User(title='{%s}', date='{%s}', content='{%s[:100]}', imagePath ='{}')>".format(
                             self.title, self.date, self.content, self.imagePath)

    @staticmethod
    def get_by_title(title):
        title = title.replace('%20', ' ')
        return BlogPost.query.filter_by(title=title).first()

    @staticmethod
    def blogposts_page(pagenum):
        blogposts = BlogPost.query.order_by(desc(BlogPost.id)).paginate(pagenum, 2 ,error_out=False)
        return blogposts


# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))
#     posts = db.relationship()
