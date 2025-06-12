from database import get_database_connection

class User:
    """
    Represents the user model with database operations.
    """

    @staticmethod
    def get_all_users():
        """
        Retrieve all users from the database.
        Returns a list of dictionaries.
        """
        try:
            connection = get_database_connection()
            cursor = connection.cursor()
            
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            return [dict(user) for user in users]
        
        except Exception as error:
            print(f"Error retrieving users: {error}")
            return []
        
        finally:
            if connection:
                connection.close()

    @staticmethod
    def create_user(name, email):
        """
        Insert a new user into the database.
        Returns a success message or error dictionary.
        """
        try:
            connection = get_database_connection()
            cursor = connection.cursor()
            
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (name, email)
            )
            connection.commit()
            return {"message": "User created successfully."}
        
        except Exception as error:
            return {"error": str(error)}
        
        finally:
            if connection:
                connection.close()
