from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url, Length, Email, Regexp, EqualTo, url, ValidationError


class BlogPostForm(Form):
    title = StringField("BlogPost title", validators = [DataRequired()], default="")
    published = BooleanField("Select whether post should be published", default="")
    imagePath = StringField(label='The url for post background image:', validators = [DataRequired()], default="")
    content = TextAreaField("BlogPost content", validators = [DataRequired()], default="")
    tags = StringField("Tags", default="")


class CommentForm(Form):
    sender = StringField("Name", validators = [DataRequired()], default="")
    content = TextAreaField("BlogPost content", validators = [DataRequired()], default="")
    level = IntegerField("Comment level")
