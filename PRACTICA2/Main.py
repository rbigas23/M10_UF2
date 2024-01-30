import psycopg2
from connection import get_connection
from create_table import create_table
from create import create_data
from read import read_data
from update import update_data
from delete import delete_data

try:
    connection = get_connection()
    cursor = connection.cursor()

    create_table(connection, cursor)

    create_data(connection, cursor)
    read_data(cursor)
    update_data(connection, cursor)
    delete_data(connection, cursor, 1)

    read_data(cursor)
    
except (Exception, psycopg2.Error) as error:
    print(f"Error: {error}")
    
finally:
    connection.close()
