##from flask import Blueprint, jsonify, render_template, request, redirect
#import os
#from web_app.models import Songs, db
#import psycopg2
#from web_app.predictions import find_similar
from dotenv import load_dotenv 

songs_routes = Blueprint("songs_routes")

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

@songs_routes.route("/fetch/<artist>/<song_name>")
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
    #Songs(track_name=song_name)



# for i in column:
#     if artist_name == i[0]
#     print(artist_id)

# for i in column:
#     for v in i:
#         if name == value:
#             do stuff



# for row in df:
#     if row['track_name'] == track_name:
#         return row['track_id']

# for row in df:
#     if row['track_id'] == track_id[0]:
#         row['track_name']

# build a route that takes in a track name and converts a track name to a track id

# feed that track id to the model, nn model

# model will return 5 most similar songs

# possibly convert track id to track name