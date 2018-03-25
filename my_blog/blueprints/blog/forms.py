from flask_wtf import Form
from wtforms.fields import StringField, BooleanField, TextAreaField, \
    IntegerField
from wtforms.validators import DataRequired


class BlogPostForm(Form):
    title = StringField("BlogPost title",
                        validators=[DataRequired()],
                        default="")
    published = BooleanField("Select whether post should be published",
                             default="")
    imagePath = StringField(label='The url for post background image:',
                            validators=[DataRequired()], default="")
    content = TextAreaField("BlogPost content",
                            validators=[DataRequired()], default="")
    tags = StringField("Tags", default="")


class CommentForm(Form):
    sender = StringField("Name:",
                         validators=[DataRequired(
                             'Please provide a valid name')])
    content = TextAreaField("Comment:",
                            validators=[DataRequired(
                                'Please fill the comment field')])
    level = IntegerField("Comment level")
