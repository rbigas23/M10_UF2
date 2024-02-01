"""
Aquesta funció ens mostra els diferents registres de la taula movies.
Si no en té cap, ho notifica.
"""

def read_data(cursor):
    read_query = "SELECT * FROM public.MOVIES"

    cursor.execute(read_query)
    result = cursor.fetchall()
    if result:
        for row in result:
            print(
                f"""
                ID: {row[0]}
                TITOL: {row[1]}
                ANYO: {row[2]}
                DURACIO: {row[3]}
                PUNTUACIO: {row[4]}
                VOTS: {row[5]}
                """
            )
    else:
        print("\nLa taula no té registres.")
