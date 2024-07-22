import pytest
import config
import datetime
import requests
from init_testdb import init_db
import endpoints
from app import create_app as frontend_app
from endpoints import create_app as backend_app

class TestBackend():
    def test_config(self):
        init_db()
        assert not backend_app().testing

    class TestData():
        timestamp = datetime.datetime.now()
        def test_add_timestamp(self):
            ct = self.timestamp
            URL = config.url + '/dataAll'
            PARAMS = {'dir':True, 'timestamp': ct}
            r = requests.post(url = URL, params=PARAMS)
            assert r.json() == None

        def test_fetch_data(self):
            date = datetime.date.today()
            URL = config.url + '/dataDate'
            PARAMS = {'date': date}
            r = requests.get(url = URL, params=PARAMS)
            assert r.json() == [ {"data": [[timestamp]]},  None]

    class TestUser():
        username = "testUser"
        password = 'password'
        def test_add_user(self):
            date = datetime.date.today()
            URL = config.url + '/user'
            PARAMS = {'username': self.username, 'password':self.password}
            r = requests.post(url = URL, params=PARAMS)
            assert r.json() == [{'data': True}, None]

        def test_fetch_user(self):
            date = datetime.date.today()
            URL = config.url + '/user'
            PARAMS = {'username': self.username, 'password':self.password}
            r = requests.get(url = URL, params=PARAMS)
            print(r.json())
            assert r.json() == [{'data': [['testUser', 'password']]}, None]

        def test_delete_user(self):
            date = datetime.date.today()
            URL = config.url + '/user'
            PARAMS = {'username': self.username, 'password':self.password}
            r = requests.delete(url = URL, params=PARAMS)
            assert r.json() == [{'data': True}, None]

        def test_fetch_user_fail(self):
            date = datetime.date.today()
            URL = config.url + '/user'
            PARAMS = {'username': self.username, 'password':self.password}
            r = requests.get(url = URL, params=PARAMS)
            print(r.json())
            assert r.json() == [{'data': []}, 'User not found']
class TestFrontend():
    app = frontend_app()
    client = app.test_client()
    def test_fetch_home(self):
        response = self.client.get('/')
        assert response.status_code == 200
    def test_fetch_data_analysis(self, client):
        response = client.get('/DataAnalysis/')
        assert response.status_code == 200
    def test_fetch_settings(self, client):
        response = client.get('/Settings/')
        assert response.status_code == 200