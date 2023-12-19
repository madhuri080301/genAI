import mysql.connector

# Replace placeholders with your Cloud SQL connection details
db_config = {
    'user': 'root',
    'password': 'APK@123',
    'host': '34.69.160.105',
    'database': 'db1',
}

try:
    # Establish a connection
    connection = mysql.connector.connect(**db_config)

    # Perform database operations here

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()