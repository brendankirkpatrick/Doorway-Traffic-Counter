import os
import psycopg2
import config

def init_db():
        conn = psycopg2.connect(
                host=config.host,
                database=config.database,
                user=config.username,
                password=config.password)

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Create base appUsers
        cur.execute('DROP TABLE IF EXISTS "appUsers";')
        cur.execute('CREATE TABLE "appUsers" (username varchar(60), password varchar(180), Primary Key(username));')

        cur.execute('INSERT INTO "appUsers" (username, password)' 'VALUES (%s, %s)',('admin','12345Admin!'))

        # create timestamp table
        cur.execute('DROP TABLE IF EXISTS "data";')
        cur.execute('CREATE TABLE "data" (direction boolean, timestamp timestamp, Primary Key(timestamp));')
        cur.execute('INSERT INTO "data" (direction, timestamp)' 'VALUES (%s, %s)',('True','2020-12-30 00:00:00'))
        conn.commit()

        cur.close()
        conn.close()


