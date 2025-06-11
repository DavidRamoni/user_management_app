# User Management App

Simple **User Management** web app built with Python and Flask, using SQLite3 database.  
Demonstrates basic **CRUD** operations with clean, object-oriented code and error handling.

---

## Features

- List all users (GET /users)  
- Add new user (POST /users) with JSON body (`name` and `email`)  
- Uses SQLite3 for storage  
- Error handling with try-except  
- Clear comments and code easy to understand  
- Example full-stack Python project  

---

## Requirements

- Python 3.7+  
- Flask  
- SQLite3  

---

## Installation & Running

1. Clone repository:

bash
git clone https://github.com/DavidRamoni/user_management_app.git

2. Change directory:
cd user_management_app

3. Install dependencies:
pip install -r requirements.txt

## How to Run

Run the application with:
python app.py
The server will start on http://127.0.0.1:5000.

# API Endpoints
GET /users
Returns a list of all users in JSON format.

POST /users
Adds a new user. Requires a JSON body with "name" and "email" fields.

# Code Structure
app.py - Main Flask application file

database.py - Handles SQLite3 database connection and operations

models.py - Defines User class and CRUD methods

README.md - Project documentation

# Notes
The code is written in English, with detailed comments and structured for easy understanding.

Feel free to clone and modify it for your own projects.

# Contact
If you want to collaborate or have questions, feel free to contact me via GitHub or email.

Thank you for checking out my project!