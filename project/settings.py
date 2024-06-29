import flask, flask_migrate, flask_sqlalchemy, os

shop = flask.Flask(
    import_name = "project",
    template_folder = "templates",
    instance_path = os.path.abspath(__file__ + "/..")
)
shop.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DB = flask_sqlalchemy.SQLAlchemy(app = shop)
migrate = flask_migrate.Migrate(app = shop, db = DB)