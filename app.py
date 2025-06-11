# app.py
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Class for managing the database
class Database:
    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self.create_users_table()

    def create_users_table(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE
                    )
                ''')
                conn.commit()
        except Exception as e:
            print("Error creating table:", e)

    def add_user(self, name, email):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            return None
        except Exception as e:
            print("Error inserting user:", e)
            return None

    def get_all_users(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users')
                return cursor.fetchall()
        except Exception as e:
            print("Error retrieving users:", e)
            return []

db = Database()

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    user_id = db.add_user(name, email)
    if user_id:
        return jsonify({"message": "User created", "id": user_id}), 201
    else:
        return jsonify({"error": "User could not be created (duplicate or error)"}), 400

@app.route('/users', methods=['GET'])
def list_users():
    users = db.get_all_users()
    users_list = [{"id": u[0], "name": u[1], "email": u[2]} for u in users]
    return jsonify(users_list)

if __name__ == "__main__":
    app.run(debug=True)
