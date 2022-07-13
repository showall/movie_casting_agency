import os
import json
from flask import Flask, request, abort, jsonify, redirect, render_template, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import random
from sqlalchemy import except_all
from werkzeug import Response
from authlib.integrations.flask_client import OAuth
from urllib.parse import quote_plus, urlencode
from models import setup_db, create_sample, Movie, Artist, Casting
from auth import AuthError, requires_auth, get_token_auth_header
from settings import AUTH0_DOMAIN,ALGORITHMS,API_AUDIENCE, YOUR_CLIENT_ID, YOUR_CALLBACK_URI, YOUR_CLIENT_SECRET, APP_SECRET_KEY

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app,support_credentials=True)
  setup_db(app)
  create_sample()
  app.secret_key = APP_SECRET_KEY
  oauth = OAuth(app)

  oauth.register(
      "auth0",
      client_id=YOUR_CLIENT_ID,
      client_secret=YOUR_CLIENT_SECRET,
      client_kwargs={
          "scope": "openid profile email",
      },
      server_metadata_url=f'https://{AUTH0_DOMAIN}/.well-known/openid-configuration'
  )

  @app.after_request
  def after_request(response):
      response.headers.add(
          "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
      )
      response.headers.add(
          "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
      )
      return response


  @app.route("/login")
  def login():
      return oauth.auth0.authorize_redirect(
          redirect_uri=url_for("callback", _external=True)
      )


  @app.route("/callback", methods=["GET", "POST"])
  def callback():
      token = oauth.auth0.authorize_access_token()
      print(token)
      session["user"] = token
      return redirect("/")


  @app.route("/logout")
  def logout():
      session.clear()
      return redirect(
          "https://" + AUTH0_DOMAIN
          + "/v2/logout?"
          + urlencode(
              {
                  "returnTo": url_for("home", _external=True),
                  "client_id": YOUR_CLIENT_ID,
              },
              quote_via=quote_plus,
          )
      )


  @app.route("/")
  def home():
    return render_template("home.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))

  # @app.route("/login2")
  # def login2():
  #   return redirect(f"https://{AUTH0_DOMAIN}/authorize?audience={API_AUDIENCE}&response_type=token&client_id={YOUR_CLIENT_ID}&redirect_uri={YOUR_CALLBACK_URI}")


  @app.route("/actors")
  @cross_origin()
  @requires_auth('get:actors-details')
  def retrieve_actors(jwt):
      artist = Artist.query.all()
      artist = [item.standard() for item in artist]
      return jsonify(
          {
              "result": artist,
          }
      )

  @app.route("/movies")
  @cross_origin()  
  @requires_auth('get:movies-details')
  def retrieve_movies(jwt):
      movie = Movie.query.all()
      movie = [item.standard() for item in movie]
      return jsonify(
          {
              "result": movie,
          }
      )

  @app.route("/casting")
  @cross_origin()
  @requires_auth('get:casting-details')
  def retrieve_casting(jwt):
      casting = Casting.query.all()
      casting = [item.standard() for item in casting]
      return jsonify(
          {
              "result": casting,
          }
      )
  @app.route("/actors/<id>",  methods=["GET","PATCH"])
  @cross_origin()
  @requires_auth('edit:actors')
  def query_specific_actors(jwt,id):
    try:
      artist = Artist.query.filter(Artist.id==id).one()
      if request.method == 'PATCH': 
        if artist:
          try:
            body = request.get_json()
            first_name = body.get('first_name',None)
            last_name = body.get('last_name',None)
            gender = body.get('gender',None)
            dateofbirth = body.get('dateofbirth',None)
            if first_name is not None:
              artist.first_name = first_name
            if last_name is not None:
              artist.last_name = last_name
            if gender is not None:
              artist.gender = gender
            if dateofbirth is not None:
              artist.dateofbirth = dateofbirth
            artist.update()
          except Exception as e:
              print(e)
              abort(422)
        return jsonify(
            {
                "result": [artist.standard()],
            }
        )

      else:
        return jsonify(
            {
                "result": [artist.standard()],
            }
        )
    except Exception as e:
      abort(404)


  @app.route("/movies/<id>",  methods=["GET","PATCH"])
  @cross_origin()
  @requires_auth('edit:movies')
  def query_specific_movies(jwt,id):
    try:
      movie = Movie.query.filter(Movie.id==id).one_or_none()
      if request.method == 'PATCH': 
        if movie:
          try:
            body = request.get_json()
            title = body.get('title',None)
            genre = body.get('genre',None)
            released_year = body.get('released_year',None)
            duration_mins = body.get('duration_mins',None)
            if title is not None:
              movie.title = title
            if genre is not None:
              movie.genre = genre
            if released_year is not None:
              movie.released_year = released_year
            if duration_mins is not None:
              movie.duration_mins = duration_mins
            movie.update()
          except Exception as e:
              abort(422)
        return jsonify(
            {
                "result": [movie.standard()],
            }
        )

      else:
        return jsonify(
            {
                "result": [movie.standard()],
            }
        )
    except Exception as e:
      abort(404)
    


  @app.route("/casting/<id>",  methods=["GET","PATCH"])
  @cross_origin()
  @requires_auth('edit:casting')
  def query_specific_casting(jwt,id):
    casting = Casting.query.filter(Casting.id==id).one_or_none()
    if request.method == 'PATCH': 
      if casting:
        try:
          body = request.get_json()
          actor_id = body.get('actor_id',None)
          movie_id = body.get('movie_id',None)
          name_of_role = body.get('name_of_role',None)
          if actor_id is not None:
            casting.actor_id = actor_id
          if movie_id is not None:
            casting.movie_id = movie_id
          if name_of_role is not None:
            casting.name_of_role = name_of_role
          casting.update()
        except Exception as e:
            print(e)
            abort(422)
      return jsonify(
          {
              "result": [casting.standard()],
          }
      )

    else:
      return jsonify(
          {
              "result": [casting.standard()],
          }
      )


  @app.route("/actors/",  methods=["POST"])
  @cross_origin()
  @requires_auth('add:actors')
  def add_actors(jwt):
    if request.method == 'POST':
      try:
        body = request.get_json()
        first_name = body.get('first_name',None)
        last_name = body.get('last_name',None)
        gender = body.get('gender',None)
        dateofbirth = body.get('dateofbirth',None)
        artist = Artist(first_name,last_name,gender,dateofbirth)
        artist.insert()
      except Exception as e:
          abort(422)
      return jsonify(
          {
              "result": [artist.standard()],
          }
      )


  @app.route("/movies",  methods=["POST"])
  @cross_origin()
  @requires_auth('add:movies')
  def add_movies(jwt):
    if request.method == 'POST':
      try:
        body = request.get_json()
        title = body.get('title',None)
        genre = body.get('genre',None)
        released_year = body.get('released_year',None)
        duration_mins = body.get('duration_mins',None)
        movie = Movie(title,genre,released_year,duration_mins)
        movie.insert()
      except Exception as e:
          abort(422)
      return jsonify(
          {
              "result": [movie.standard()],
          }
      )

  @app.route("/casting",  methods=["POST"])
  @cross_origin()
  @requires_auth('add:casting')
  def add_casting(jwt):
    if request.method == 'POST':
      try:
        body = request.get_json()
        actor_id = body.get('actor_id',None)
        movie_id = body.get('movie_id',None)
        name_of_role = body.get('name_of_role',None)
        casting = Casting(actor_id,movie_id,name_of_role)
        casting.insert()
      except Exception as e:
          print(e)
          abort(422)
      return jsonify(
          {
              "result": [casting.standard()],
          }
      )


  @app.route("/actors/<id>/delete",  methods=["DELETE"])
  @cross_origin()
  @requires_auth('delete:actors')  
  def delete_actors(jwt,id):
    artist = Artist.query.filter(Artist.id==id).one_or_none()
    if request.method == 'DELETE': 
      artist.delete()
      return (
          jsonify(
              {
                  "deleted": str(id),
              }
          ),
          200,
      )


  @app.route("/movies/<id>/delete",  methods=["DELETE"])
  @cross_origin()
  @requires_auth('delete:movies') 
  def delete_movies(jwt,id):
    movie = Movie.query.filter(Movie.id==id).one_or_none()
    if request.method == 'DELETE': 
      movie.delete()
      return (
          jsonify(
              {
                  "deleted": str(id),
              }
          ),
          200,
      )


  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({"success": False, "error": 400,
                      "message": "bad request"}), 400

  @app.errorhandler(404)
  def ressource_not_found(error):
      return (jsonify({"success": False, "error": 404,
                        "message": "resource not found"}), 404, )

  @app.errorhandler(405)
  def method_not_allowed(error):
      return (jsonify({"success": False, "error": 405,
                        "message": "method not allowed"}), 405, )

  @app.errorhandler(422)
  def unprocessable(error):
      return (
          jsonify({"success": False,
                    "error": 422,
                    "message": "unprocessable"
                    }),
          422,
      )

  @app.errorhandler(500)
  def internal_server_error(error):
      return (
          jsonify(
              {"success": False,
                "error": 500,
                "message": "internal server error"
                }
          ),
          500,
      )

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)