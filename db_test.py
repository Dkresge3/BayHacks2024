import mysql.connector

def test_db_connection(host, user, password, database):
    try:
        # Attempt to connect to the MySQL server
        connection = mysql.connector.connect(
            host="Localhost",
            user="root",
            password="Smartcollar",
            database="smartcollar_db"
        )
        
        # Check if the connection is successful
        if connection.is_connected():
            print("Connection to MySQL database successful!")
            # Close the connection
            connection.close()
        else:
            print("Connection to MySQL database failed.")
    
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)

# Replace these with your MySQL server details
host = "localhost"
user = "your_username"
password = "your_password"
database = "your_database"

# Test the database connection
test_db_connection(host, user, password, database)
