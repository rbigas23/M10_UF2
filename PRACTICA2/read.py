def read_data(cursor):
    read_query = "SELECT * FROM public.MOVIES"

    cursor.execute(read_query)
    result = cursor.fetchall()

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
