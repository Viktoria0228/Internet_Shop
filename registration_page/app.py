import flask

registr = flask.Blueprint(
    name = "registration",
    import_name = "registration_page",
    template_folder = "templates",
    static_folder = "static",
    static_url_path = "/registration"
)