from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url, Length, Email, Regexp, EqualTo, url, ValidationError


class LoginForm(Form):
    username = StringField("User name", validators = [DataRequired()])
    password = StringField("Password", validators = [DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    error = StringField()
