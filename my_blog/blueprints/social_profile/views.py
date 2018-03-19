from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
profile_fb = make_facebook_blueprint(
    client_id="216836045536768",
    client_secret="d52377110e46f51c6b1f788ed091ff28",
)

@profile_fb.route("/")
def connect():
    if not facebook.authorized:
        return  redirect(url_for("github.login")) #render_template('facebook.html') #
    resp = facebook.get("/user")
    assert resp.ok
    return "You are @{login} on Facebook".format(login=resp.json()["login"])



from flask_dance.contrib.google import make_google_blueprint, google
profile_google = make_google_blueprint(
    client_id="216836045536768",
    client_secret="d52377110e46f51c6b1f788ed091ff28",
    scope=["profile", "email"]
)

@profile_google.route("/")
def connect():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    return "You are @{email} on Google".format(email=resp.json()["email"])



from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
profile_twitter = make_twitter_blueprint(
    api_key="216836045536768",
    api_secret="d52377110e46f51c6b1f788ed091ff28",
)

@profile_twitter.route("/")
def connect():
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("account/settings.json")
    assert resp.ok
    return "You are @{login} on Twitter".format(login=resp.json()["screen_name"])
