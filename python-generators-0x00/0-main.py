import seed
print("Starting script...")
connection = def connect_db():
if connection:
    print("Connected to MySQL")
    seed.create_database(connection)
    connection.close()
    print("connection successful")

    connection = seed.connect_to_prodev()
    if connection:
        print("Connected to ALX_prodev DB")
        seed.create_table(connection)
        seed.insert_data(connection, 'user_data.csv')
        print("Data insertion done")

        cursor = connection.cursor()
        cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';")
        result = cursor.fetchone()
        if result:
            print("Database ALX_prodev is present")

        cursor.execute("SELECT * FROM user_data LIMIT 5;")
        rows = cursor.fetchall()
        print("Sample rows:", rows)
        cursor.close()
