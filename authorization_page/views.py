import flask
import flask_login
from registration_page.models import User
from project.settings import DB
from flask_login import current_user
from registration_page.views import is_registered

def render_authorization_page():
    if flask.request.method == "POST":
        for user in User.query.filter_by(name = flask.request.form.get("name")):
            if user.password == flask.request.form['password']:
                flask_login.login_user(user)
                return flask.redirect("/")
                    
    return flask.render_template(template_name_or_list = "authorization.html", is_registered = is_registered)