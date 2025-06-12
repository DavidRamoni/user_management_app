from flask import Flask, request, jsonify
from database import initialize_database
from models import User

# Initialize Flask application
app = Flask(__name__)

# Create the users table if it does not exist
initialize_database()

@app.route('/users', methods=['GET'])
def get_users():
    """
    GET /users
    Returns the list of all users in JSON format.
    """
    try:
        users = User.get_all_users()
        return jsonify(users), 200
    except Exception as error:
        return jsonify({"error": f"Failed to get users: {str(error)}"}), 500

@app.route('/users', methods=['POST'])
def create_user():
    """
    POST /users
    Creates a new user from JSON input (name and email).
    """
    try:
        data = request.get_json()

        # Extract name and email from request
        name = data.get('name')
        email = data.get('email')

        # Validate required fields
        if not name or not email:
            return jsonify({"error": "Both name and email are required."}), 400

        # Insert new user
        result = User.create_user(name, email)

        if "message" in result:
            return jsonify(result), 201
        else:
            return jsonify(result), 400

    except Exception as error:
        return jsonify({"error": f"Failed to create user: {str(error)}"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
