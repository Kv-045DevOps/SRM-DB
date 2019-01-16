import psycopg2
import os


def connect_db(dbname):
    if dbname != str(os.getenv("PGDATABASE")):
        raise ValueError("Couldn't not find DB with given name")
    conn = psycopg2.connect(host=str(os.getenv("POSTGRES_HOST")),
                           port=str(os.getenv("POSTGRES_PORT")), 
                           user=str(os.getenv("PGUSER")),
                           password=str(os.getenv("PGPASSWORD")),
                           dbname=str(os.getenv("PGDATABASE")))
    return conn