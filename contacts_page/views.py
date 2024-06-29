import flask, flask_login

def render_contacts_page():
    return flask.render_template(template_name_or_list = "contacts.html", is_authenticated = flask_login.current_user.is_authenticated)