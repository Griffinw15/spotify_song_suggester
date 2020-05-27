#__init__.py

import os
from flask import Flask

from web_app.models import db, migrate

from web_app.routes import route

from dotenv import load_dotenv


DATABASE_URI = "postgres://henlxuqj:aeumGWYFAxsOULrbEIRxQ2LfktUlBWMH@ruby.db.elephantsql.com:5432/henlxuqj"

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # suppress warning messages
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(route)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)