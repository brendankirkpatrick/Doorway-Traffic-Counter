from flask import Flask, render_template
import requests
import psycopg2
import config
import os
import endpoints
import datetime
from init_db import init_db

def create_app():
    app = Flask(__name__)
    init_db()
    return app

app = create_app()

def addTimestamp():
    ct = datetime.datetime.now()
    URL = config.url + '/dataAll'
    PARAMS = {'dir':True, 'timestamp': ct}
    r = requests.post(url = URL, params=PARAMS)
    return r.json()

def fetchData():
    date = datetime.date.today()
    URL = config.url + '/dataDate'
    PARAMS = {'date': date}
    r = requests.get(url = URL, params=PARAMS)
    print(r.json())

@app.route('/')
def homePage():
    # addTimestamp()
    # fetchData()
    # return render_template('index.html' )
    return '<h1>helloworld</h1>'

@app.route('/DataAnalysis/')
def dataPage():
    return render_template('DataAnalysis.html' )

@app.route('/Settings/')
def settingsPage():
    return render_template('Settings.html')