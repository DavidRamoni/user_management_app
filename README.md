# 🧑‍💻 User Management API

A clean, lightweight RESTful API built with Flask and SQLite3 for managing users.  
Includes proper code structure, object-oriented programming (OOP), error handling, and documentation.

---

## 📦 Features

- Modular Python architecture
- SQLite3 database integration
- Object-Oriented Programming (OOP)
- Full CRUD support (Create, Read)
- Clean error handling with try-except
- Written in clear, beginner-friendly English
- Ideal for small internal tools or quick user demos

---

## 🗂️ Project Structure

user_management_app/
│
├── app.py # Main Flask app: API routes
├── database.py # Database connection and initialization
├── models.py # User model with CRUD methods
├── users.db # SQLite3 database (auto-created)
├── requirements.txt # List of dependencies
└── README.md # Project documentation


---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.9+
- pip (Python package manager)

---

### 🛠️ Installation

bash
# Clone the repository
git clone https://github.com/DavidRamoni/user_management_app.git
cd user_management_app

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# By default, the server will run on:
http://127.0.0.1:5000

# API Endpoints
POST /users

Body (JSON):
{
  "name": "David Ramoni",
  "email": "davidramoni123@gmail.com"
}

Response:
{
  "message": "User created successfully."
}

# Get All Users (GET)
GET /users

Response:
[
  {
    "id": 1,
    "name": "David Ramoni",
    "email": "davidramoni123@gmail.com"
  },
  ...
]

# Example Test (using curl)
# Add a user
curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d "{\"name\": \"David Ramoni\", \"email\": \"davidramoni123@gmail.com\"}"

# Get users
curl http://127.0.0.1:5000/users

# Author
David Ramoni
Full Stack Python Developer
Email: [davidramoni123@gmail.com]
GitHub: https://github.com/DavidRamoni

Contributing
Contributions, suggestions, and improvements are welcome.
Feel free to fork the repository and submit pull requests.