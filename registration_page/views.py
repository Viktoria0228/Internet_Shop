import flask, flask_login
from .models import User
from project.settings import DB
from project.settings import shop

is_registered = False
def render_registration_page():
    global is_registered
    # print("User.query in reg: ", User.query.all())
    print("flask.request.method =", flask.request.method)
    
    if flask.request.method == "POST":
        print("Post")
        if flask.request.form['password1'] == flask.request.form['password2']:   
            users = User( 
                name = flask.request.form['name'],
                email = flask.request.form['email'],
                password = flask.request.form['password1'],
                password_confirmation = flask.request.form["password2"]
            )
            print("12")
            if flask_login.current_user.is_authenticated:
                # print("Ви вже авторизовані")
                return "Ви вже авторизовані"
            else:
                for user in User.query.filter_by(name = flask.request.form['name']):
                    if user.password == flask.request.form['password1']:
                        flask_login.login_user(user)
                        # return flask.redirect("/")
            try:
                DB.session.add(users)
                DB.session.commit()
                print("user registered")
                is_registered = True
                # return flask.redirect("/")
                
            except:
                return "ERROR"
            else:
                pass
    return flask.render_template(template_name_or_list = "registration.html", is_registered = is_registered)

