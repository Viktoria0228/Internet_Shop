import flask

def show_basket_page():
    return flask.render_template(template_name_or_list = "basket.html")