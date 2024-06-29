import flask, flask_login, flask
from shop_page.models import Product
from flask_mail import Message
from project.mail_config import mail
from project.settings import DB
from .models import Order


waiting = False
def render_cart_page():
    global waiting
    list_products = []
    repeat_id = []
    products_quantity = {}
    if flask.request.cookies:
        print(flask.request.cookies.get("products").split(" "))
        products = flask.request.cookies.get("products").split(" ")
        for id_product in products:
            count_products = products.count(id_product)
            chosen_element = id_product
            print("count_products =", count_products)
            print("id_product =", id_product)
            print("products =", products)
            print("id_product =", id_product)
            if chosen_element in products_quantity:
                print("chosen_element in products_quantity")
                products_quantity[id_product] += 1
            else:
                products_quantity[id_product] = 1
            print("products_quantity =", products_quantity)
            if id_product not in repeat_id:
                print("\n","count_products =", count_products, "\n", "list_products =", list_products)
                print("Product.query.get(id_product) = ", Product.query.get(id_product))
                if Product.query.get(id_product) != None: 
                    list_products.append(Product.query.get(id_product))
                    repeat_id.append(id_product)
        try:
            if list_products[-1].count <= count_products:
                list_products[-1].count = count_products
        except:
            return "Корзина порожня😢"
        
        if flask.request.method == "POST":

            print("flask form", flask.request.form)
            orders = Order(
                name = flask.request.form['name'],
                surname = flask.request.form['surname'],
                email = flask.request.form['email'],
                phone_number = flask.request.form["phone_number"],
                city_recepient = flask.request.form["city_recepient"],
                post_office = flask.request.form["post_office"],
                add_wishes = flask.request.form["add_wishes"]
                
            )
            DB.session.add(orders)
            DB.session.commit()

            for product in list_products:
                name_product = product.name
            msg = Message(
                subject = 'Вітаємо з придбанням!!!',
                recipients = [flask_login.current_user.email],
                body = f'Ви придбали товар {name_product}' 
            )
            # mail.send(msg)

            waiting = True

                   
        return flask.render_template(
            template_name_or_list = "cart.html",
            products = list_products,
            quantity = products_quantity,
            is_authenticated = flask_login.current_user.is_authenticated,
            waiting = waiting
        )
    else:    
        return flask.render_template(template_name_or_list = "cart.html", is_authenticated = flask_login.current_user.is_authenticated)