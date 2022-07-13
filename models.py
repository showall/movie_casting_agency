#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from faulthandler import dump_traceback
import os
import re
from unicodedata import name
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from settings import DB_NAME, DB_USER, DB_PASSWORD

database_name = 'casting_agency'
database_name = DB_NAME
database_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,'localhost:5432',DB_NAME)

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.drop_all()
    db.create_all()


def create_sample():
    # add 2 demo row which is helping in POSTMAN test
    movie = Movie(
        title='Dr Strange',
        genre='mystery',
        released_year=2022,
        duration_mins=200
    )


    artist = Artist(
        first_name ='Benedict',
        last_name ='Cumberbatch',
        gender="male",
        dateofbirth="01-01-1980",
    )

    casting = Casting(
        actor_id=1,
        movie_id=1,
        name_of_role="Stephen Strange",
    )
    movie.insert()
    artist.insert()
    casting.insert()

    movie = Movie(
        title='Iron Man',
        genre='Action',
        released_year=2008,
        duration_mins=120
    )


    artist = Artist(
        first_name ='Robert',
        last_name ='Downey',
        gender="male",
        dateofbirth="01-01-1980",
    )

    casting = Casting(
        actor_id=2,
        movie_id=2,
        name_of_role="Tony Stark",
    )
    movie.insert()
    artist.insert()
    casting.insert()

"""
Artist

"""
class Artist(db.Model):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    dateofbirth = Column(String)#datetime
    casting = db.relationship('Casting', backref="artists",lazy=True, cascade="all, delete")

    def __init__(self, first_name, last_name, gender, dateofbirth):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.dateofbirth = dateofbirth

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def standard(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'dateofbirth': self.dateofbirth
            }

"""
Movie

"""
class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String) #put as 1 first
    released_year = Column(Integer)
    duration_mins = Column(Integer)
    casting = db.relationship('Casting', backref="movies",lazy=True, cascade="all, delete")

    def __init__(self, title, genre,released_year,duration_mins):
        self.title = title
        self.genre = genre
        self.released_year = released_year
        self.duration_mins = duration_mins

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def standard(self):
        return {
            'id': self.id,
            'title': self.title,
            "genre" : self.genre,
            "released_year" : self.released_year,
            "duration_mins" : self.duration_mins                        
            }

class Casting(db.Model):  #association_table
    __tablename__ = 'casting'

    id = Column(Integer, primary_key=True)
    actor_id = Column(Integer, db.ForeignKey('artists.id'))
    movie_id = Column(Integer, db.ForeignKey('movies.id'))
    name_of_role = Column(String)

    def __init__(self, actor_id, movie_id,name_of_role):
        self.actor_id = actor_id
        self.movie_id = movie_id
        self.name_of_role = name_of_role       
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit() 

    def standard(self):
        return {
            'actor_id': self.actor_id,
            'movie_id': self.movie_id,
            "role" : self.name_of_role
            }