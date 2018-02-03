from flask import url_for, render_template
from FlaskBlogSite import app

@app.route('/')
@app.route('/index')
def index():
	"""
	Generate main web page
	"""
	return render_template('base.html')
