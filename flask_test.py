from app import app
import unittest


class FlaskappTests(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_users_status_code(self):
        # sends HTTP GET request to the application
        result = self.app.get('/api/v1/users')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_tweets_status_code(self):
        # sends HTTP GET request to the application
        result = self.app.get('/api/v2/tweets')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_info_status_code(self):
        # sends HTTP GET request to the application
        result = self.app.get('/api/v1/info')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_1delusers_none_404(self): 
        # sends HTTP Delete request to the application 
        result = self.app.delete('/api/v1/users', data='{"username":"xuser1"}', content_type='application/json') 
        # assert the status code of the response 
        self.assertEquals(result.status_code, 404)       
    def test_2addusers_status_code(self):
        # sends HTTP POST request to the application
        result = self.app.post('/api/v1/users', data='{"username":"xuser1", "email": "xuser1@gmail.com", "password": "xyz"}',content_type='application/json')
        print(result)
        # assert the status code of the response
        self.assertEquals(result.status_code, 201)       

    def test_3addusers_conflict_409(self):
        # sends HTTP POST request to the application
        result = self.app.post('/api/v1/users', data='{"username":"xuser1", "email": "xuser1@gmail.com", "password": "test123"}',content_type='application/json')
        print(result)
        # assert the status code of the response
        self.assertEquals(result.status_code, 409)


    def test_4updusers_status_code(self): 
        # sends HTTP PUT request to the application 
        # on the specified path 
        result = self.app.put('/api/v1/users/24', data='{"password":"testing123"}', content_type='application/json') 
        # assert the status code of the response 
        self.assertEquals(result.status_code, 200) 

    def test_5delusers_status_code(self): 
        # sends HTTP Delete request to the application 
        result = self.app.delete('/api/v1/users', data='{"username":"xuser1"}', content_type='application/json') 
        # assert the status code of the response 
        self.assertEquals(result.status_code, 200)         