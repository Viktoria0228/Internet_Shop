import flask

contacts = flask.Blueprint(
    name = "contacts",
    import_name = "contacts_page",
    static_folder = "static",
    template_folder = "templates",
    static_url_path = "/static"
)