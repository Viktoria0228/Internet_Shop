import flask


shop = flask.Blueprint(
    name = 'shop',
    import_name = 'shop_page',
    template_folder = 'templates',
    static_folder = "static",
    static_url_path = "/shop/"
)