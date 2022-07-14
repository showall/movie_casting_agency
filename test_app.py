import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, abort, jsonify, redirect, render_template, session, url_for
from sqlalchemy import Column, String, Integer, create_engine
from app import create_app
from models import setup_db, Movie, Artist, Casting, create_sample
from settings import DB_NAME, DB_USER, DB_PASSWORD, BEARER_TOKEN_FULLACCESS,DB_NAME_HEROKU


executive_producer_auth_header = {
    'Authorization': BEARER_TOKEN_FULLACCESS
}

inv_executive_producer_auth_header = {
    'Authorization': "BEARER XXX"
}


class TestCase(unittest.TestCase):
    """This class represents the test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        #self.app = create_app()
        self.app = create_app(test=True)       
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,'localhost:5432',self.database_name)
        #self.database_path = '{}'.format(DB_NAME_HEROKU,DB_NAME)
        setup_db(self.app, self.database_path,test=True)
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            #self.db.drop_all()   
            #self.db.create_all()
        create_sample()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

#----------------------------------------------------------------------------#
# Tests for GET '/movies'
#----------------------------------------------------------------------------#

    def test_get_movies(self):
        res = self.client().get('/movies',headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 200)

    def test_get_movie_wo_auth(self):
        res = self.client().get('/movies',headers = inv_executive_producer_auth_header)
        self.assertEqual(res.status_code, 403)

#----------------------------------------------------------------------------#
# Tests for GET '/actors'
#----------------------------------------------------------------------------#

    def test_get_actors(self):
        res = self.client().get('/actors',headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 200)

    def test_get_actors_wo_auth(self):
        res = self.client().get('/actors',headers = inv_executive_producer_auth_header)
        self.assertEqual(res.status_code, 403)

#----------------------------------------------------------------------------#
# Tests for POST '/movies'
#----------------------------------------------------------------------------#

    def test_post_movies(self):
        request = {
            "duration_mins": 150,
            "genre": "action",
            "released_year": 2018,
            "title": "Thor:God of Thunder"
        }
        res = self.client().post('/movies', json = request,headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 200)

    def test_post_invalid_movies(self):
        request = {
            "duration_mins": 150,
            "genred": "action",
            "released_year": 2018,
            "title": "Thor:God of Thunder"
        }
        res = self.client().post('/movies', json = request,headers = inv_executive_producer_auth_header)
        self.assertEqual(res.status_code, 403)

#----------------------------------------------------------------------------#
# Tests for GET '/actors/<id>'
#----------------------------------------------------------------------------#

    def test_get_specific_actor(self):
        res = self.client().get('/actors/1',headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 200)

    def test_get_invalid_specific_actor(self):
        res = self.client().post('/actors/1',headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 405)


#----------------------------------------------------------------------------#
# Tests for GET '/movies/<id>'
#----------------------------------------------------------------------------#

    def test_get_specific_movie(self):
        res = self.client().get('/movies/1',headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 200)

    def test_get_specific_movie(self):
        res = self.client().get('/movies/100000',headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 404)


#----------------------------------------------------------------------------#
# Tests for PATCH '/actors/<id>'
#----------------------------------------------------------------------------#

    def test_patch_specific_actor(self):
        request = {
            "dateofbirth": "01-01-1977"
        }
        res = self.client().patch('/actors/1',json = request, headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 200)

    def test_inv_patch_specific_actor(self):
        request = {
            "dateofbirth": "01-01-1977"
        }    
        res = self.client().put('/actors/1',headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 405)


#----------------------------------------------------------------------------#
# Tests for PATCH '/movies/<id>'
#----------------------------------------------------------------------------#

    def test_patch_specific_movie(self):
        request = {
            "genre": "sci-fi",
        }
        res = self.client().patch('/movies/1',json = request, headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 200)

    def test_inv_patch_specific_movie(self):
        request = {
            "genre": "sci-fi",
        }
        res = self.client().patch('/movies/1',json = request, headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 200)


#----------------------------------------------------------------------------#
# Tests for DELETE '/actors/<id>/delete'
#----------------------------------------------------------------------------#

    def test_delete_specific_actor(self):
        res = self.client().delete('/actors/1',headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 200)

    def test_delete_specific_actor(self):
        res = self.client().delete('/actors/1',headers = inv_executive_producer_auth_header)
        self.assertEqual(res.status_code, 405)


#----------------------------------------------------------------------------#
# Tests for DELETE '/movies/<id>/delete'
#----------------------------------------------------------------------------#

    def test_delete_specific_movie(self):
        res = self.client().delete('/movies/1',headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 200)

    def test_delete_specific_movie(self):
        res = self.client().delete('/movies/100000',headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 405)


if __name__ == "__main__":
    unittest.main()
