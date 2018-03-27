from flask_wtf import FlaskForm
from wtforms.fields import StringField, BooleanField, TextAreaField, \
    IntegerField
from wtforms.validators import DataRequired


class BlogPostForm(FlaskForm):
    title = StringField("BlogPost title", validators=[DataRequired()])
    published = BooleanField("Publish", default="")
    imagePath = StringField(label='Background image url:',
                            validators=[DataRequired()], default="")
    content = TextAreaField("Post content", validators=[DataRequired()])
    tags = StringField("Tags", default="")


class CommentForm(FlaskForm):
    sender = StringField(
        "Name:", validators=[DataRequired('Please provide a valid name')])
    content = TextAreaField(
        "Comment:", validators=[DataRequired('Please fill the comment field')])
    level = IntegerField("Comment level")
