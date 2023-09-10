import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import app
from models import setup_db, Actors, Movies

class CastingAgencyTestCase(unittest.TestCase):
    def setUp(self):
        ASSISTANT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaVTVwUHdVb0dSS1lBbDFYTmhndiJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktZnVsbHN0YWNrd2ViLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNTE3Mjk3MDY2NDIzMDE1NTg1MCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNjk0MzU5NzA1LCJleHAiOjE2OTQzNjY5MDUsImF6cCI6IkZaMXo2UmJjWjYxeVphNFYydDViV2RyRlJNbVBOUFloIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.bjjDly-Y7uKG9k_KlKeXoHqhVcXeyY5zI1pezKemEYEfZij2bcrJiNEG9r4CDTthbw3IGq9LLX4_RL4GBQvocuFUcYhlSJnzmzKmJxJ3bB58G9vfpH0ziyU7A4FVrGedyyVrJIi47omzCtO4nTY5_7bxZHM5P94_dXYNzxg7iA9ngOERxgD0cyd5Refdr36sKNq1WeGnThr_CpXu8EMkYfNHClnw5v4f-N6wVeV_QTdbtl9l3LxrNmogSKmIKdQFenhHN6Q-QOzsl_4bznnJwG8oRDeviWquXuBbg-hUjVevkXFo1zi6Wrwfp-Rub6p_303lWdqVeKZGO94Yv99vvQ'
        DIRECTOR_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaVTVwUHdVb0dSS1lBbDFYTmhndiJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktZnVsbHN0YWNrd2ViLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNDU5MjA2MjUwMTIzMDgyMzk4OSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNjk0MzYwMDk0LCJleHAiOjE2OTQzNjcyOTQsImF6cCI6IkZaMXo2UmJjWjYxeVphNFYydDViV2RyRlJNbVBOUFloIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.VsXdBlXmDJJFW5Jegyo4lLxeeF4UB8-1Fk93M-OoNovzYbaHHZ5giyEKw1MxefziEExQ_q0o3bzU4D9vWvRH2KayY0O5v3_khaz-jIVlG7I8rN6q6TxvCt69cXjMMRoq7O8EoD1lhJ06fqhwvV2ysvNN5hTIEVczMRn6X8j9eFcDubCocUretKRLdoYidPiIp5cGcL6OfCMFGlh9i0LDag0QNcvU24xv3mujSrVqCZ4kHDiowDm4FS-UG7IRCb92zZV0bjqZpB7XLXWn-GLxQ0jvIkUlFtaH5k6XbNg43fqrZ_4PjeZUwHDP2507NfMq1zQEpvsC5BMDG2Mo6QAx5Q'
        PRODUCER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaVTVwUHdVb0dSS1lBbDFYTmhndiJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktZnVsbHN0YWNrd2ViLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNzY5NjA3MjY3MTkzMTI4MjI5MSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNjk0MzU5NTQ2LCJleHAiOjE2OTQzNjY3NDYsImF6cCI6IkZaMXo2UmJjWjYxeVphNFYydDViV2RyRlJNbVBOUFloIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.ZuZtK1t-REzUEWNh_ToGXE_5Kc-rEGmD3uMGVIok3f0-CQig5mdqJIWuUQNUvGxTB-GAQYexdAVgVXWPOsaC7GOCXpvyIyqglfRQMRDeb4Bzk4SRTKC7GbSmpi7d_Hsuv4VosBiGHt22ZvRcihEQjatW5FVtiAx6Kpg_b0sTOe_PNYE-1tjMc7hwfTt39uy5TLVK3PEN9v7rYRkh3Tz-BuqKX8aNMcnAyKHmbFS0mn50xGoZ2zR7Rfp0OSk4sOyTKDvznuNXmkvvjUm8jPxLwgoaTFH_7237hecgOSqNClPFgEkNpQFBpqRH-FgREL8YunMGPX3MVH99urX_GIh0Dg'

        self.director_header = {'Authorization': 'Bearer ' + DIRECTOR_TOKEN}
        self.assistant_header = {'Authorization': 'Bearer ' + ASSISTANT_TOKEN}
        self.producer_header = {'Authorization':'Bearer ' + PRODUCER_TOKEN}
        self.app = app
        self.client = self.app.test_client
        setup_db(self.app)

        self.post_actor = {
            'name': "Michael",
            'age': 45,
            'gender': 'MALE'
        }

        self.post_actor1 = {
            'name': "George",
            'age': 28,
            'gender': 'MALE'
        }

        self.post_actor2 = {
            'name': "Markus",
            'age': 39,
            'gender': 'MALE'
        }

        self.post_actor_name_missing = {
            'age': 34,
            'gender': "MALE"
        }

        self.post_actor_gender_missing = {
            'age': 34,
            'name': "John"
        }

        self.patch_actor_on_age = {
            'age': 55
        }

        self.post_movie = {
            'title': "SAMPLE MOVIE",
            'release_date': "2090-10-10"
        }

        self.post_movie1 = {
            'title': "MAHABHARATA",
            'release_date': "2030-10-10"
        }

        self.post_movie2 = {
            'title': "MAHABHARATA - 2",
            'release_date': "2032-10-10"
        }

        self.post_movie_title_missing = {
            'release_date': "2030-10-10"
        }

        self.post_movie_reldate_missing = {
            'title': "RAMAYANA"
        }

        self.patch_movie_on_reldate = {
            'release_date': "2035-10-10"
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_actors1(self):
        res = self.client().get('/actors?page=1',
                                headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) > 0)

    def test_get_actors2(self):
        res = self.client().get('/actors?page=1',
                                headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) > 0)

    def test_get_actors3(self):
        res = self.client().get('/actors?page=1',
                                headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) > 0)

    def test_post_new_actor1(self):
        res = self.client().post('/actors',
                                 json=self.post_actor1,
                                 headers=self.director_header)
        data = json.loads(res.data)

        actor = Actors.query.filter_by(id=data['actor-added']).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsNotNone(actor)

    def test_post_new_actor2(self):
        res = self.client().post('/actors',
                                 json=self.post_actor2,
                                 headers=self.producer_header)
        data = json.loads(res.data)

        actor = Actors.query.filter_by(id=data['actor-added']).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsNotNone(actor)

# - Director Role
    def test_post_new_actor_name_missing(self):
        res = self.client().post('/actors',
                                 json=self.post_actor_name_missing,
                                 headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'unprocessable')

    def test_post_new_actor_gender_missing(self):
        res = self.client().post('/actors',
                                 json=self.post_actor_gender_missing,
                                 headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_actor(self):
        res = self.client().post('/actors', json=self.post_actor,
                                 headers=self.director_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        actor_id = data['actor-added']

        res = self.client().delete('/actors/{}'.format(actor_id),
                                   headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actor-deleted'], actor_id)

    def test_delete_actor_not_found(self):
        res = self.client().delete('/actors/999',
                                   headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Not found')

    def test_patch_actor(self):
        res = self.client().patch('/actors/2',
                                  json=self.patch_actor_on_age,
                                  headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actor-updated'], 2)

    def test_patch_actor_not_found(self):
        res = self.client().patch('/actors/99',
                                  json=self.patch_actor_on_age,
                                  headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Not found')

# RBAC - Test Cases:
    def test_get_actors_no_auth(self):
        res = self.client().get('/actors?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'],
                         'Authorization header is expected.')

# RBAC POST actors with wrong Authorization header - Assistant Role
    def test_post_actor_wrong_auth(self):
        res = self.client().post('/actors',
                                 json=self.post_actor1,
                                 headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found.')

# RBAC DELETE Negative Case - Delete an existing actor
# without appropriate permission
    def test_delete_actor_wrong_auth(self):
        res = self.client().delete('/actors/10',
                                   headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found.')


# Test cases for the Endpoints related to /movies
# ------------------------------------------------
# GET Positive case - Assistant Role


    def test_get_movies1(self):
        res = self.client().get('/movies?page=1',
                                headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movies']) > 0)

# GET Positive case - Director Role
    def test_get_movies2(self):
        res = self.client().get('/movies?page=1',
                                headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movies']) > 0)

# GET Positive case - Producer Role
    def test_get_movies3(self):
        res = self.client().get('/movies?page=1',
                                headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movies']) > 0)

# POST Positive case - Producer Role
    def test_post_new_movie2(self):
        res = self.client().post('/movies', json=self.post_movie2,
                                 headers=self.producer_header)
        data = json.loads(res.data)

        movie = Movies.query.filter_by(id=data['movie-added']).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsNotNone(movie)

# POST Negative Case - Add movie with missing title
# - Producer Role
    def test_post_new_movie_title_missing(self):
        res = self.client().post('/movies',
                                 json=self.post_movie_title_missing,
                                 headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'unprocessable')

# POST Negative Case - Add movie with missing release date
# - Producer Role
    def test_post_new_movie_reldate_missing(self):
        res = self.client().post('/movies',
                                 json=self.post_movie_reldate_missing,
                                 headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'unprocessable')

# DELETE Positive Case - Deleting an existing movie - Producer Role
    def test_delete_movie(self):
        res = self.client().post('/movies',
                                 json=self.post_movie,
                                 headers=self.producer_header)
        data = json.loads(res.data)

        movie_id = data['movie-added']

        res = self.client().delete('/movies/{}'.format(movie_id),
                                   headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['movie-deleted'], movie_id)

# DELETE Negative Case movie not found - Producer Role
    def test_delete_movie_not_found(self):
        res = self.client().delete('/movies/777',
                                   headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Not found')

# PATCH Positive case - Update Release Date of
# an existing movie - Director Role
    def test_patch_movie(self):
        res = self.client().patch('/movies/2',
                                  json=self.patch_movie_on_reldate,
                                  headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['movie-updated'], 2)

# PATCH Negative case - Update Release Date for
# non-existent movie - Director Role
    def test_patch_movie_not_found(self):
        res = self.client().patch('/movies/99',
                                  json=self.patch_movie_on_reldate,
                                  headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Not found')

# RBAC - Test Cases:
# RBAC GET movies w/o Authorization header
    def test_get_movies_no_auth(self):
        res = self.client().get('/movies?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'],
                         'authorization_header_missing')

# RBAC POST movies with wrong Authorization header - Director Role
    def test_post_movie_wrong_auth(self):
        res = self.client().post('/movies', json=self.post_movie1,
                                 headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found')

# RBAC DELETE Negative Case - Delete an existing movie
# without appropriate permission
    def test_delete_movie_wrong_auth(self):
        res = self.client().delete('/movies/8',
                                   headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found')


# run 'python test_app.py' to start tests
if __name__ == "__main__":
    unittest.main()