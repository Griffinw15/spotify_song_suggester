#__init__.py

from flask import Flask

from model import 
from route import route

DATABASE_URI = ""

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(route)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)