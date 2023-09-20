import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import app
from models import setup_db

ASSISTANT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaVTVwUHdVb0dSS1lBbDFYTmhndiJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktZnVsbHN0YWNrd2ViLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNTE3Mjk3MDY2NDIzMDE1NTg1MCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNjk1MjE5ODQyLCJleHAiOjE2OTUyMjcwNDIsImF6cCI6IkZaMXo2UmJjWjYxeVphNFYydDViV2RyRlJNbVBOUFloIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.S0Cfo1qujij-d5aQM4W0w-V9wdB9BjPYoLmum1Zvi3Ab4IblXhEh5HqJdQV3SBNIdaJ_il8LrJCpVRXasWNrNRuR_xwR3Ddo4R35K5MDTgS__Pc0IHpJ8jv1btROXDc-V5rLkOoCJ5uInAFJalseaJJOTsfthd2E3VSSwc29vboXXTgbSSQyF3mKlSwZVO1CtHAgKsdRQwiC0wSeJGu5h-LsaYLo_p4cvtxjpXUHT-Gv2cabIGxcYRLMuYZ7YTx5BdPA0OF9tKYs5W6MCGmbSz-0m1XhPdYmaM2MahGc4KZh4iXHhW1jHmDcYZa1OgRtUn6GO00EUj5vcy5aOPYJ7Q'
DIRECTOR_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaVTVwUHdVb0dSS1lBbDFYTmhndiJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktZnVsbHN0YWNrd2ViLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNDU5MjA2MjUwMTIzMDgyMzk4OSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNjk1MjE5Njk2LCJleHAiOjE2OTUyMjY4OTYsImF6cCI6IkZaMXo2UmJjWjYxeVphNFYydDViV2RyRlJNbVBOUFloIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.D7RTzz6tkztG12xZsNsvp_tyCVeY2ZUdxLlWSpbq3LQQxMDyxgqGi5OSSgdxXKd3g5KMk0qV5CbUqlB54oGg8FDzTwUr0udm9ENdxCQKcR4lsNI0QcBR9VgTWd9jcL8m7g-wtnIHX1z8LHNwlg4RRp4aos9tgrNLfDFf8VPmNt3h6gIvlNBWQUmzTI8iDxw_zgrllvAvEFCg-PDsmkeAu7Ltlj7J7IMhVjSke6KPdG_9V1j_XiMmq4609H3SWokE2HE3tF98YtP5rGEFfbcsP8GTfNYvT_trby50_zG4q-lqSBoJsQrLOVw-RECk3XiQ3jecwBoXy3tkORU9Io890w'
PRODUCER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxaVTVwUHdVb0dSS1lBbDFYTmhndiJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktZnVsbHN0YWNrd2ViLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNzY5NjA3MjY3MTkzMTI4MjI5MSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNjk1MjE5NDg0LCJleHAiOjE2OTUyMjY2ODQsImF6cCI6IkZaMXo2UmJjWjYxeVphNFYydDViV2RyRlJNbVBOUFloIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.pOrqvl9tsdJBY7uKJBUNbXirZBFIXpxSjzcUSnrXXU-nJhCtSVCK2QpUpzhcUtuY63Mx9MRPQn5NdeDvl2u9-ldwiv_GjjBI7g9URjkMpvBrbNpZUCchFtqYUqXwj1AvTvNb4ZIh_m01xIDPLec2LaE36R83IsnOuxGk5mY84ZNinAdjw52tvqMBVT4CZZYZceZ7iblz2kzrgMdOvclGgi9_XFwArlaMtRpcrXQxUDWLI28mt9MlnP9cXXT1rRdkGYfL6LyRK9Ou7WVXUqEhYFzVIKkyd1dUIPcOFKEByRLyjsoFSPTDMP9BOa2e103FCQh9oRs4UFHSiL88TmxtQg'


class CastingAgencyTestCase(unittest.TestCase):
    def setUp(self):
        self.director_header = {'Authorization': 'Bearer ' + DIRECTOR_TOKEN}
        self.assistant_header = {'Authorization': 'Bearer ' + ASSISTANT_TOKEN}
        self.producer_header = {'Authorization': 'Bearer ' + PRODUCER_TOKEN}
        self.app = app
        self.client = self.app.test_client
        setup_db(self.app)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def test_get_actors_success(self):
        res = self.client().get('/actors', headers=self.director_header)
        data = json.loads(res.data)
        self.assertTrue(data['success'])

    def test_get_actors_fail(self):
        res = self.client().get('/actors', headers='')
        data = json.loads(res.data)
        self.assertFalse(data['success'])

    def test_get_movies_success(self):
        res = self.client().get('/movies', headers=self.assistant_header)
        data = json.loads(res.data)
        self.assertTrue(data['success'])

    def test_get_movies_fail(self):
        res = self.client().get('/movies', headers='')
        data = json.loads(res.data)
        self.assertFalse(data['success'])

    def test_delete_actors_success(self):
        actor = {
            'name': '1',
            'age': 12,
            'gender': 'man'
        }
        res_post = self.client().post('/actors', json=actor, headers=self.producer_header)
        data_post = json.loads(res_post.data)
        self.assertTrue(data_post['success'])
        res = self.client().delete(
            '/actors/' + str(data_post['actor']['id']), headers=self.producer_header)
        data = json.loads(res.data)
        self.assertTrue(data['success'])

    def test_delete_actors_fail(self):
        actor = {
            'name': '1',
            'age': 12,
            'gender': 'man'
        }
        res_post = self.client().post('/actors', json=actor, headers=self.director_header)
        data_post = json.loads(res_post.data)
        self.assertTrue(data_post['success'])
        res = self.client().delete(
            '/actors/' + str(data_post['actor']['id']), headers=self.assistant_header)
        data = json.loads(res.data)
        self.assertFalse(data['success'])

    def test_delete_movie_success(self):
        movie = {
            "title": "test1",
            "release_date": "02/12/2024"
        }
        res_post = self.client().post('/movies', json=movie, headers=self.producer_header)
        data_post = json.loads(res_post.data)
        self.assertTrue(data_post['success'])
        res = self.client().delete(
            '/movies/' + str(data_post['movie']['id']), headers=self.producer_header)
        data = json.loads(res.data)
        self.assertTrue(data['success'])

    def test_delete_movie_fail(self):
        movie = {
            "title": "test1",
            "release_date": "02/12/2024"
        }
        res_post = self.client().post('/movies', json=movie, headers=self.assistant_header)
        data_post = json.loads(res_post.data)
        self.assertFalse(data_post['success'])
        if data_post['success'] != False:
            res = self.client().delete(
                '/movies/' + str(data_post['movie']['id']), headers=self.assistant_header)
            data = json.loads(res.data)
            self.assertFalse(data['success'])

    def test_post_movie_success(self):
        movie = {
            "title": "test1",
            "release_date": "02/12/2024"
        }
        res_post = self.client().post('/movies', json=movie, headers=self.producer_header)
        data_post = json.loads(res_post.data)
        self.assertTrue(data_post['success'])

    def test_post_movie_fail(self):
        movie = {
            "title": "test1",
            "release_date": "02/12/2024"
        }
        res_post = self.client().post('/movies', json=movie, headers=self.assistant_header)
        data_post = json.loads(res_post.data)
        self.assertFalse(data_post['success'])

    def test_post_actors_success(self):
        actor = {
            'name': '1',
            'age': 12,
            'gender': 'man'
        }
        res_post = self.client().post('/actors', json=actor, headers=self.producer_header)
        data_post = json.loads(res_post.data)
        self.assertTrue(data_post['success'])

    def test_post_actors_fail(self):
        actor = {
            'name': '1',
            'age': 12,
            'gender': 'man'
        }
        res_post = self.client().post('/actors', json=actor, headers=self.assistant_header)
        data_post = json.loads(res_post.data)
        self.assertFalse(data_post['success'])


if __name__ == "__main__":
    unittest.main()
