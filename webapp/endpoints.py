from flask import jsonify
import os
import psycopg2
import config
from init_db import init_db 

def get_db_connection():
    conn = psycopg2.connect(
        host=config.host,
        database=config.database,
        user=config.username,
        password=config.password)
    return conn

def user(username, password, method):
    conn = get_db_connection()
    cur = conn.cursor()
    error = None
    data = None
    if method == "GET":
        userInfo = None
        try:
            cur.execute('SELECT * FROM "appUsers" where username=%s and password=%s;', (username, password))
            userInfo = cur.fetchall()
        except:
            error = "SQL Error"
            cur.close()
            conn.close()
            return  jsonify({"data":[]}, error)
        if(userInfo != None and len(userInfo) == 1):
            
            cur.close()
            conn.close()
            return  jsonify({"data":userInfo, "error": error})
        else:
            error = "User not found"
            cur.close()
            conn.close()
            return  jsonify({"data":userInfo, "error": error})
    elif method == "POST":
        data = False
        try:
            cur.execute('INSERT INTO "appUsers" (username, password)'
                    'VALUES (%s, %s)',
                    (username, password))
            conn.commit()
            data = True
        except:
            error = "SQL Error"
        cur.close()
        conn.close()
        return  jsonify({"data":data, "error": error})
    elif method == "DELETE":
        success = False
        try:
            cur.execute('DELETE FROM "appUsers" where username=%s and password=%s;', (username, password))
            conn.commit()
            success = True
        except:
            error = "SQL Error"
        cur.close()
        conn.close()
        return  jsonify({"data":success, "error": error})
    else: 
        error = "Invalid Method"
        cur.close()
        conn.close()
        return  jsonify({"data":[], "error": error})

def dataAll(dir, timestamp, method):
    conn = get_db_connection()
    cur = conn.cursor()
    error = None
    data = None
    if method == "GET":
        try:
            cur.execute('SELECT * FROM "data"')
            data = cur.fetchall()
        except:
            error = "SQL Error"
        cur.close()
        conn.close()
        return  jsonify({"data":data}, {"error": error})
    if method == "POST":
        try:
            cur.execute('INSERT INTO "data" (direction, timestamp)'
                        'VALUES (%s, %s)',
                        (dir, timestamp))
            conn.commit()
        except:
            error = "SQL Error"
        cur.close()
        conn.close()
        return  jsonify(error)
    else: 
        error = "Invalid Method"
        cur.close()
        conn.close()
        return  jsonify({"data":[], "error": error})


def dataOnDate(date, method):
    conn = get_db_connection()
    cur = conn.cursor()
    dateStart = date + ' 00:00:00'
    dateEnd = date + ' 24:00:00'
    error = None
    data = None
    acc = []
    if method == "GET":
        try:
            cur.execute('SELECT * FROM "data" where timestamp between %s and %s', (dateStart, dateEnd))
            data = cur.fetchall()
            peopleIn = 0
            peopleOut = 0
            for moment in data:
                if( moment[0] == True):
                    peopleIn += 1
                else:
                    peopleOut += 1
            acc.append(peopleIn)
            acc.append(peopleOut)
        except:
            error = "SQL Error"
        cur.close()
        conn.close()
        return  jsonify({"data":acc, "error": error})
    else: 
        error = "Invalid Method"
        cur.close()
        conn.close()
        return  jsonify({"data":[], "error": error})
