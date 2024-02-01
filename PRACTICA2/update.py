"""
Aquesta funció modifica un dels registres de la taula.
"""

def update_data(connection, cursor):
    update_query = "UPDATE public.MOVIES SET ANYO = 1999 WHERE TITOL = 'Titanic'"
    cursor.execute(update_query)
    connection.commit()
    print(f"\nActualització efectuada sense errors.")