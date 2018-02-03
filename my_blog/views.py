from flask import url_for, render_template

@app.route('/')
@app.route('/index')
def index():
	"""
	Generate main web page
	"""
	return render_template('base.html')
