#__init__.py

import os
from flask import Flask

from web_app.models import db, migrate

#from web_app.routes import home_routes, songs_routes

import psycopg2

from dotenv import load_dotenv

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

DATABASE_URL = "postgres://henlxuqj:aeumGWYFAxsOULrbEIRxQ2LfktUlBWMH@ruby.db.elephantsql.com:5432/henlxuqj"

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # suppress warning messages
    db.init_app(app)
    migrate.init_app(app, db)

    #app.register_blueprint(home_routes)
    #app.register_blueprint(songs_routes)
    

    @app.route("/")
    def home_page():
        return "go to /fetch/artist/trackname to query the model!"

    @app.route("/fetch/<artist>/<song_name>")
    def song_recommender(artist=None, song_name=None):
    # query = f"""
    # SELECT track_id from Songs where Songs.name = {song_name}
    # """

        query = f"SELECT track_id from Songs where Songs.name = '{song_name}'"
        conpg = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD,
                                host=DB_HOST)
        curpg = conpg.cursor()
        curpg.execute(query)
        track_id = curpg.fetchall()
        track_id[0][0]
        loaded_model = pickle.load(open('finalizedmodel.sav', 'rb'))
        data = loaded_model.predict(track_id)
        music = []
        for i in data:
            query2 = f"SELECT Songs.name from Songs where Songs.track_id = '{i}'"
            curpg.execute(query2)
            track_name = curpg.fetchall()
            music.append(track_name[0][0])
            #music.append(track_name)
        return music
        conpg.commit()
        conpg.close()
    return app

#if __name__ == "__main__":
my_app = create_app()
my_app.run(debug=True)