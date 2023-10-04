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

# Close the connection when done
connection.close()
