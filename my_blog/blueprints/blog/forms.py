from flask_wtf import FlaskForm
from wtforms.fields import StringField, BooleanField, TextAreaField, \
    IntegerField
from wtforms.validators import DataRequired

from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileAllowed

images = UploadSet('images', IMAGES)


class BlogPostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    published = BooleanField("Publish", default="")
    imagePath = StringField(label='Background image url:')
    content = TextAreaField("Content", validators=[DataRequired()])
    tags = StringField("Tags", default="")
    upload = FileField('image', validators=[
        FileAllowed(images, 'Images only!')
    ])


class CommentForm(FlaskForm):
    sender = StringField(
        "Name:", validators=[DataRequired('Please provide a valid name')])
    content = TextAreaField(
        "Comment:", validators=[DataRequired('Please fill the comment field')])
    level = IntegerField("Comment level")
