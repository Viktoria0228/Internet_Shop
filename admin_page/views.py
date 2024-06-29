import flask, os, flask_login
from shop_page.models import Product
from project.settings import DB
def render_admin_page():
    if flask.request.method == "POST":
        print("flask.request.form.get('change') =", flask.request.form.get("change"))
        try:
            print(flask.request.form.get("del"))
            if flask.request.form.get("change"):
                list_new_value = flask.request.form.get("change").split("^")
                # print("new_value.split[-1] = ",list_new_value[2])
                print("new_value.split('^') = ", list_new_value)
                product = Product.query.get(list_new_value[1])
                print(product)
                if len(list_new_value) == 2:
                    product.image = list_new_value[0]
                elif list_new_value[-1] == "name":
                    product.name = list_new_value[0]
                elif list_new_value[-1] == "price":
                    product.price = list_new_value[0]
                elif list_new_value[-1] == "discount":
                    product.discount = list_new_value[0]
                
                DB.session.commit()
                
                
            elif flask.request.form.get("del") == None:
                print("db new product")
                product = Product(
                    image = flask.request.form["image"],
                    name = flask.request.form["name"],
                    description = flask.request.form["description"],
                    price = flask.request.form["price"],
                    discount = flask.request.form["discount"],
                    count = flask.request.form["count"]
                )
                DB.session.add(product)
                DB.session.commit()

                image = flask.request.files["image"]
                image.save(os.path.abspath(__file__ + f"/../../shop_page/static/images/{product.name}.jpg"))
            else:
                # pass
                product_id = int(flask.request.form["del"])
                product_del = Product.query.get(product_id)
                # print("product_del:", product_del)
                if Product.query.get(product_id):
                    DB.session.delete(product_del)
                    DB.session.commit()
                    os.remove(os.path.abspath(__file__ + f"/../../shop_page/static/images/{product_del.name}.jpg"))

        except Exception as e:
            print(e)
        
    return flask.render_template(template_name_or_list = "admin.html", products = Product.query.all(), is_authenticated = flask_login.current_user.is_authenticated)