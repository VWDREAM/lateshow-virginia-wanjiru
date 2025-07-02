# 🎬 Late Show API

A Flask RESTful API for managing **Late Show episodes**, **guests**, and their **appearances**.

---

## 📌 Project Description

This application provides a backend API for storing and managing data about guest appearances on a fictional Late Show. It includes relationships between guests, episodes, and appearances, data validations, and JSON serialization.

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Flask CORS
- SQLite (for development)
- Postman (for API testing)

---

## ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/lateshow-your-name.git
cd lateshow-your-name

2. **Create and Activate Virtual Environment
    python3 -m venv venv
    source venv/bin/activate
3. **Install Dependencies
    pip install -r requirements.txt

4.**Run Migrations
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    Seed the Database

    python -m app.seed
5. ***Run the Server
    flask run
