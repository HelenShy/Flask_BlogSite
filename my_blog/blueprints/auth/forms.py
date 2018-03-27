from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, \
    BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("User name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    error = StringField()
