import flask, pandas, os, flask_login
from project.settings import DB
from .models import Product
def render_shop_page():
    # Product.query.delete()

    print("Product.query.all():", Product.query.all)
    # if Product.query.all() == :
    if True:
        print("1")
        path_xlsx = os.path.abspath(__file__  + "/../phones_flask_project.xlsx")
        print("2")
        read_xlsx = pandas.read_excel(
            io = path_xlsx,
            header = None,
            names = ["name", "price", "description", "count", "image", "discount"]
        )

        Product.query.delete()
        print(read_xlsx)
        for row in read_xlsx.iterrows():
            row_data = row[1]
            # print(row_data)
            product = Product(
                name = row_data['name'],
                price = row_data['price'],
                description = row_data['description'],
                count = row_data['count'],
                image = row_data['image'],
                discount = row_data["discount"]
            )
            print("product =", product)
            DB.session.add(product)

        DB.session.commit()

    return flask.render_template(
        template_name_or_list = "shop.html",
        products = Product.query.all(),
        is_authenticated = flask_login.current_user.is_authenticated
    )