def create_data(connection, cursor):
    insert_query = "INSERT INTO public.MOVIES(ID, TITOL, ANYO, DURACIO, PUNTUACIO, VOTS) VALUES ('1', 'Titanic', '2001', 125, 9.1, 21512)"
    cursor.execute(insert_query)
    connection.commit()
    print("\nDades inserides sense errors.")
