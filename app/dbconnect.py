import psycopg2
from app import config


def connect_db(dbname):
    if dbname != config.DATABASE_CONFIG['dbname']:
        raise ValueError("Couldn't not find DB with given name")
    conn = psycopg2.connect(host=config.DATABASE_CONFIG['host'],
                           user=config.DATABASE_CONFIG['user'],
                           password=config.DATABASE_CONFIG['password'],
                           dbname=config.DATABASE_CONFIG['dbname'])
    return conn