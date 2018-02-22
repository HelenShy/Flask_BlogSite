from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
@main.route('/index')
def index():
	"""
	Generate main web page
	"""
	return render_template('home.html')
