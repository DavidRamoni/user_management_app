import sqlite3

def get_database_connection():
    """
    Establish and return a connection to the SQLite database.
    Uses Row factory to access columns by name.
    """
    try:
        connection = sqlite3.connect('users.db')
        connection.row_factory = sqlite3.Row
        return connection
    except sqlite3.Error as error:
        print(f"Database connection error: {error}")
        raise

def initialize_database():
    """
    Create the 'users' table if it does not exist.
    """
    try:
        connection = get_database_connection()
        cursor = connection.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error initializing database: {error}")
    finally:
        if connection:
            connection.close()
