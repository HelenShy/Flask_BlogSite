from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url, Length, Email, Regexp, EqualTo, url, ValidationError


class BlogPostForm(Form):
    title = StringField("BlogPost title", validators = [DataRequired()])
    published = BooleanField("Select whether post should be published")
    imagePath = StringField(label='The url for post background image:', validators = [DataRequired()])
    content = StringField("BlogPost content", validators = [DataRequired()])

    def validate(self):
        if not Form.validate(self):
            return False
        return True
