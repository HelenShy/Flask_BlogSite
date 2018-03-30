import os
from flask import redirect, url_for, session, request, flash, Blueprint
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from flask_dance.contrib.github import make_github_blueprint, github
from flask_dance.contrib.google import make_google_blueprint, google

from .models import UserProfile

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

page_referrer = ''


profile = Blueprint('profile', __name__, template_folder='templates')


@profile.route("/login/<provider>")
def login(provider):
    global redirect_to, page_referrer
    if 'page_referrer' not in session:
        session['page_referrer'] = request.referrer
    if 'current_profile' in session:
        redirect_to = session['page_referrer']
        del session['page_referrer']
        return redirect(redirect_to)
    if provider == 'google':
        return redirect(url_for('google.connect_google'))
    if provider == 'facebook':
        return redirect(url_for('facebook.connect_facebook'))
    if provider == 'github':
        return redirect(url_for('github.connect_github'))


@profile.route("/logout")
def logout():
    # del session['google_oauth_token']
    # facebook_oauth_token
    # github_oauth_token
    if 'current_profile' in session:
        del session['current_profile']
    flash("You have logged out")
    return redirect(request.referrer)


profile_fb = make_facebook_blueprint(
    client_id=os.getenv("FACEBOOK_CLIENT_ID"),
    client_secret=os.environ.get("FACEBOOK_CLIENT_SECRET"),
    redirect_url='/profile/login/facebook'
)


@profile_fb.route("/facebook/auth")
def connect_facebook():
    page_referrer = request.referrer
    if not facebook.authorized:
        return redirect(url_for("facebook.login"))
    resp = facebook.get("/me?fields=id,name,email,picture")
    assert resp.ok
    current_profile = UserProfile(
        name="{val}".format(val=resp.json()['name']),
        oauth_provider='facebook',
        picture_url="{val}".format(
            val=resp.json()['picture']['data']['url']))
    session['current_profile'] = current_profile.to_json()
    return redirect(page_referrer)


profile_google = make_google_blueprint(
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    scope=["profile", "email"],
    redirect_url='/profile/login/google'
)


@profile_google.route("/google/auth")
def connect_google():
    page_referrer = request.referrer
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    current_profile = UserProfile(
        name="{val}".format(val=resp.json()['name']),
        oauth_provider='google',
        picture_url="{val}".format(
            val=resp.json()['picture']))
    session['current_profile'] = current_profile.to_json()
    return redirect(page_referrer)


profile_github = make_github_blueprint(
    client_id=os.getenv("GITHUB_CLIENT_ID"),
    client_secret=os.environ.get("GITHUB_CLIENT_SECRET"),
    redirect_url='/profile/login/github'
)


@profile_github.route("/github/auth")
def connect_github():
    page_referrer = request.referrer
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    current_profile = UserProfile(
        name="{val}".format(val=resp.json()['login']),
        oauth_provider='github',
        picture_url="{val}".format(val=resp.json()['avatar_url']))
    session['current_profile'] = current_profile.to_json()
    return redirect(page_referrer)
