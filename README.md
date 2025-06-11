# User Management App

A simple Python web API to manage users using Flask and SQLite3.

## Features

- Add new users via API
- List all users
- Uses OOP and clean code
- Handles errors with try/except
- Easy to understand and extend

## Requirements

- Python 3
- Flask

##  How to run

1. Clone the repository or download the files.

2. Install dependencies:
       pip install flask

3. Run the application:
       python app.py


## API Endpoints

### POST `/users`

Create a new user.

Use **Postman** or a similar tool.

**Body (JSON):**
```json
{
"name": "John Doe",
"email": "john@example.com"
}

RESPONSE:

{
  "message": "User created",
  "id": 1
}

GET /users

List all registered users.

Open this in your browser:
http://127.0.0.1:5000/users

Technologies:
Python
Flask
SQLite3

Author
Made by [David Ramoni]