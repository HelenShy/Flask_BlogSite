from flask import render_template, redirect, url_for, session, jsonify, request
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_dance.contrib.google import make_google_blueprint, google

from .models import UserProfile


profile_fb = make_facebook_blueprint(
    client_id="216836045536768",
    client_secret="d52377110e46f51c6b1f788ed091ff28",
)


@profile_fb.route("/facebook/auth")
def connect():
    page_referrer = request.referrer
    if not facebook.authorized:
        return redirect(url_for("facebook.login"))
    resp = facebook.get("/me?fields=id,name,email,picture")
    assert resp.ok
    current_profile = UserProfile(name="{val}".format(val=resp.json()['name']),
                                  oAuthProvider='facebook',
                                  picture_url="{val}".format(val=resp.json()['picture']['data']['url']))
    session['current_profile'] = current_profile.to_json()
    return redirect(page_referrer)


profile_google = make_google_blueprint(
    client_id="1015893889816-j0hipndj0nqhjdtnk5kuddihdnvceh66.apps.googleusercontent.com",
    client_secret="jSRL5Ku517xAk0293XY3wEDE",
    scope=["profile", "email"],
)


@profile_google.route("/google/auth")
def connect():
    #del session['google_oauth_token']
    page_referrer = request.referrer
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    current_profile = UserProfile(name="{val}".format(val=resp.json()['name']), oauth_provider='google',
                                  picture_url="{val}".format(val=resp.json()['picture']))
    session['current_profile'] = current_profile.to_json()
    return redirect(page_referrer)


@profile_google.route("/logout")
def logout():
    del session['current_profile']
    return redirect(request.referrer)





profile_twitter = make_twitter_blueprint(
    api_key="1",
    api_secret="2",
)


@profile_twitter.route("/twitter/auth")
def connect():
    page_referrer = request.referrer
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("account/settings.json")
    assert resp.ok
    current_profile = UserProfile(name="{val}".format(val=resp.json()['name']), oauth_provider='google',
                                  picture_url="{val}".format(val=resp.json()['picture']))
    session['current_profile'] = current_profile.to_json()
    return redirect(page_referrer)
