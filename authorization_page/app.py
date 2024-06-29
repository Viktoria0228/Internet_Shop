import flask

auth = flask.Blueprint(
    name = "authorization_page",
    import_name = "authorization_page",
    template_folder = "templates",
    static_folder = "static",
    static_url_path = "/authorization"
)