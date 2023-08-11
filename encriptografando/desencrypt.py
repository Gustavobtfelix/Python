import bcrypt
import pyodbc  # For connecting to SQL Server

def validate_password(provided_password, stored_hashed_password):
    # Compare the provided password with the stored hashed password
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_hashed_password.encode('utf-8'))

# Connect to the database
connection = pyodbc.connect('your_connection_string_here')

# Example user data
login = "example_user"
provided_password = "user_provided_password"

# Retrieve the stored hashed password from the database
cursor = connection.cursor()
cursor.execute("SELECT senha FROM usuarios_card_printer WHERE login = ?", login)
row = cursor.fetchone()
if row:
    stored_hashed_password = row.senha

    # Validate the provided password
    if validate_password(provided_password, stored_hashed_password):
        print("Password is correct!")
    else:
        print("Password is incorrect.")
else:
    print("User not found.")
