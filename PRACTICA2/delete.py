def delete_data(connection, cursor, id):
    query = f"DELETE FROM public.MOVIES WHERE ID = {id}"
    cursor.execute(query)
    connection.commit()
    print("\nDades eliminades sense errors.")