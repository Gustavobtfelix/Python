import mysql.connector

# Replace these with your actual credentials
host = "url"
user = "your_username"
password = "your_password"
database = "your_database_name"

# Create a connection
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)


# Check if the connection was successful
if connection.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect to MySQL database")
    exit()

# Create a cursor object to interact with the database
cursor = connection.cursor()

# SELECT ALL
select_query = "SELECT * FROM your_table_name"
cursor.execute(select_query)
result = cursor.fetchall()
for row in result:
    print(row)

#SELECT ONE
select_query = "SELECT * FROM your_table_name"
cursor.execute(select_query)
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()

#INSERT
insert_query = """
INSERT INTO table (var1, var2)
VALUES ('value1', 'value2')
"""
cursor.execute(insert_query)
connection.commit()

# UPDATE
update_query = "UPDATE your_table_name SET column_name = 'new_value' WHERE condition"
cursor.execute(update_query)
connection.commit()

# DELETE
delete_query = "DELETE FROM your_table_name WHERE condition"
cursor.execute(delete_query)
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()