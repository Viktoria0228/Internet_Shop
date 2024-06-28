import flask

admin = flask.Blueprint(
    name = 'admin',
    import_name = 'admin_page',
    template_folder = 'templates',
    static_folder = "static",
    static_url_path = "/admin/"
)