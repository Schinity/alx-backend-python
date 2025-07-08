def insert_data(connection, file_path):
    cursor = connection.cursor()

    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("""
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (
                row['user_id'],
                row['name'],
                row['email'],
                row['age']
            ))

    cursor.execute("SELECT COUNT(*) FROM user_data;")
    print("Number of users in table:", cursor.fetchone()[0])

    connection.commit()
    cursor.close()
