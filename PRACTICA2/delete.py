"""
Aquesta funció elimina el registre amb una id determinada.
"""

def delete_data(connection, cursor, id):
    query = f"DELETE FROM public.MOVIES WHERE ID = {id}"
    cursor.execute(query)
    connection.commit()
    print("\nDades eliminades sense errors.")