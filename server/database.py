import psycopg2
from flask import g
import os

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            database=os.environ.get('POSTGRES_DB'),
            user=os.environ.get('POSTGRES_USER'),
            password=os.environ.get('POSTGRES_PASSWORD'),
            host=os.environ.get('POSTGRES_HOST', 'db'),
            port=os.environ.get('POSTGRES_PORT', '5432')
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
