import os

basedir = os.path.abspath("./")  # + os.path.dirname(__file__)

DEBUG = True
SECRET_KEY = 'kG2\xf3\xf1\xee\x1d\xfcV\xf0\xbbu\xeb\xe8\x1f\xf3$\xf6)\xd7?oRF'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'my_blog.db')
TRAP_BAD_REQUEST_ERRORS = True
