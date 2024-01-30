def create_table(connection, cursor):
    query = """
    CREATE TABLE MOVIES(
        ID SERIAL PRIMARY KEY,
        TITOL VARCHAR(255) NOT NULL,
        ANYO VARCHAR(255) NOT NULL,
        DURACIO BIGINT NOT NULL,
        PUNTUACIO FLOAT NOT NULL,
        VOTS VARCHAR(255) NOT NULL
    )"""

    cursor.execute(query)
    connection.commit()
    
    print("\nTaula creada sense errors.")
