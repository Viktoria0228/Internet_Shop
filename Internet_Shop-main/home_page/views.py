import flask
import flask_login

def render_home_page():
    print("flask_login.current_user.is_authenticated =", flask_login.current_user.is_authenticated)
    return flask.render_template(template_name_or_list = "home.html", is_authenticated = flask_login.current_user.is_authenticated)