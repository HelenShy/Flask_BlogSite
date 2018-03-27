from flask import Blueprint, render_template, flash, request, redirect, url_for, session
from flask_login import login_required, login_user, logout_user

from .models import User
from .forms import LoginForm
# from .url import is_safe_url

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    """
    Login and validate the user
    """
    form = LoginForm()
    form.error = None
    if request.method == 'POST':
        form.username = request.form['userName']
        form.password = request.form['password']
        form.remember_me = request.form.get('checkbox')
        user = User.get_by_username(form.username)
        if user is not None and user.check_password(form.password):
            login_user(user)
            flash('Logged in successfully.')
            # if not is_safe_url(next):
            #  	return abort(400)
            # #return redirect(next or url_for('main.index'))
            return redirect(request.args.get('next') or url_for('main.index'))
        form.error = "Please enter valid user name and password"
    return render_template('login_form.html', form=form)


@auth.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    """
    Logout the user
    """
    logout_user()
    flash('User logged out.')
    return redirect(url_for('main.index'))
