import flask_login
from .settings import shop
from registration_page.models import User

shop.secret_key = "067bbv48jbvd3sill911vbhtfjklks378zwr6h9"
# print("secret_key =", shop.secret_key)    

login = flask_login.LoginManager(shop)
login.init_app(shop)

@login.user_loader
def load(id):
    # print("id =", id)
    return User.query.get(id)