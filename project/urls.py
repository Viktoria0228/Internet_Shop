import home_page, registration_page, authorization_page, shop_page, cart_page, admin_page, contacts_page
from .settings import shop

# print("add_url_rule")
home_page.home.add_url_rule(rule = "/", view_func = home_page.render_home_page, methods = ["GET", "POST"])

registration_page.registr.add_url_rule(rule = "/registration", view_func = registration_page.render_registration_page, methods = ["GET", "POST"])

authorization_page.auth.add_url_rule(rule = "/authorization", view_func = authorization_page.render_authorization_page, methods = ["GET", "POST"])

shop_page.shop.add_url_rule(rule = "/shop", view_func = shop_page.render_shop_page, methods = ["GET", "POST"])

cart_page.cart.add_url_rule(rule = "/cart", view_func = cart_page.render_cart_page, methods = ["GET", "POST"])

contacts_page.contacts.add_url_rule(rule = "/contacts", view_func = contacts_page.render_contacts_page, methods = ["POST", "GET"])

admin_page.admin.add_url_rule(rule = "/admin/", view_func = admin_page.render_admin_page, methods = ["POST", "GET"])

# print("register blueprint")
shop.register_blueprint(blueprint = home_page.home)

shop.register_blueprint(blueprint = registration_page.registr)

shop.register_blueprint(blueprint = authorization_page.auth)

shop.register_blueprint(blueprint = shop_page.shop)

shop.register_blueprint(blueprint = cart_page.cart)

shop.register_blueprint(blueprint = contacts_page.contacts)

shop.register_blueprint(blueprint = admin_page.admin)