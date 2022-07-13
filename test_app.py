import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, create_engine
from app import create_app
from models import setup_db, Movie, Artist, Casting, create_sample
from settings import DB_NAME, DB_USER, DB_PASSWORD, BEARER_TOKEN_FULLACCESS


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
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,'localhost:5432',self.database_name)

        setup_db(self.app, self.database_path)
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
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
# Tests for GET '/movies/<id>/delete'
#----------------------------------------------------------------------------#

    def test_delete_specific_movie(self):
        res = self.client().delete('/movies/1',headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 200)

    def test_delete_specific_movie(self):
        res = self.client().delete('/movies/100000',headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 405)

















# #----------------------------------------------------------------------------#
# # Tests for GET '/categories/${id}/questions'
# #----------------------------------------------------------------------------#
#     def test_get_questions_by_categoryid(self):
#         res = self.client().get('/categories/2/questions')
#         self.assertEqual(res.status_code, 200)
#     def test_post_questions_by_categoryid(self):
#         res = self.client().post('/categories/2/questions')
#         self.assertEqual(res.status_code, 405)








#----------------------------------------------------------------------------#
# Tests for GET '/actors'
#----------------------------------------------------------------------------#

    def test_get_categories(self):
        res = self.client().get('/movies',headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 200)

    def test_post_categories(self):
        request = {
            "duration_mins": 150,
            "genre": "action",
            "released_year": 2018,
            "title": "Thor:God of Thunder"
        }
        res = self.client().post('/movies', json = request,headers = executive_producer_auth_header)
        self.assertEqual(res.status_code, 200) #method not allowed

#----------------------------------------------------------------------------#
# # Tests for GET '/questions?page=${integer}'
# #----------------------------------------------------------------------------#
#     def test_get_questions_with_pagination(self):
#         res = self.client().get('/questions?page=1')
#         self.assertEqual(res.status_code, 200)

#     def test_delete_questions_with_pagination(self):
#         """Test if could delete entire page"""
#         res = self.client().delete('/questions?page=1000')
#         self.assertEqual(res.status_code, 405)

# #----------------------------------------------------------------------------#
# # Tests for GET '/categories/${id}/questions'
# #----------------------------------------------------------------------------#
#     def test_get_questions_by_categoryid(self):
#         res = self.client().get('/categories/2/questions')
#         self.assertEqual(res.status_code, 200)
#     def test_post_questions_by_categoryid(self):
#         res = self.client().post('/categories/2/questions')
#         self.assertEqual(res.status_code, 405)

# #-------------------------------------------------h---------------------------#
# # Tests DELETE '/questions/${id}'
# #----------------------------------------------------------------------------#
    
#     def test_delete_question(self):
#         last_id = Question.query.order_by(Question.id).first().id # contains id from last created category
#         res = self.client().delete('/questions/'+str(last_id))
#         self.assertEqual(res.status_code, 200)

#     def test_delete_invalid_question(self):
#         invalid_id = 0
#         res = self.client().delete('/questions/'+str(invalid_id))
#         self.assertEqual(res.status_code, 422) 

# #----------------------------------------------------------------------------#
# # Tests for POST '/quizzes'
# #----------------------------------------------------------------------------#
#     def test_post_quiz(self):
#         request = {
#         "previous_questions": [1, 4, 20, 15],
#         "quiz_category": {"type":'Science',"id":1}
#         }

#         res = self.client().post('/quizzes', json = request)
#         self.assertEqual(res.status_code, 200)
    
#     def test_post_quiz_with_invalid_category(self):
#         request = {
#         "previous_questions": [1, 4, 20, 15],
#         "quiz_category": {"type":'science',"id":1}
#         }
#         res = self.client().post('/quizzes', json = request)
#         self.assertEqual(res.status_code, 422)

# #----------------------------------------------------------------------------#
# # Tests for POST '/questions'
# #----------------------------------------------------------------------------#

#     def test_post_question(self):

#         # Used as header to POST /question
#         request = {
#         'question':  'Heres a new question string',
#         'answer':  'Heres a new answer string',
#         'difficulty': 1,
#         'category': 3,
#          }

#         res = self.client().post('/questions', json = request)
#         self.assertEqual(res.status_code, 200)

#     def test_post_invalid_question(self):
#         """Test POST a new question with missing category """
#         invalid_request = {
#         'questions':  'Heres a new question string',
#         'answer':  'Heres a new answer string',
#         'difficulty': 1
#          }
#         res = self.client().post('/questions', json = invalid_request)
#         self.assertEqual(res.status_code, 422)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
