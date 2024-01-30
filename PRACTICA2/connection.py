import psycopg2

arguments = {
    "database": "postgres",
    "user": "user_postgres",
    "password": "pass_postgres",
    "host": "localhost",
    "port": "5432",
}


def get_connection():
    return psycopg2.connect(**arguments)
