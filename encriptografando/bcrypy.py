import bcrypt
import pyodbc  # For connecting to SQL Server

def hash_password(password):
    # Generate bcrypt hash
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    return hashed_password

# Connect to the database
connection = pyodbc.connect('your_connection_string_here')

# Example user data
login = "example_user"
password = "my_secure_password"

# Hash the password
hashed_password = hash_password(password)

# Store the hashed password in the database
cursor = connection.cursor()
cursor.execute("INSERT INTO usuarios_card_printer (login, senha) VALUES (?, ?)", login, hashed_password)
connection.commit()

print("Password stored securely.")
