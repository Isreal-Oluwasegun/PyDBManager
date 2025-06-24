# PyDBManager

**PyDBManager** is a lightweight Python utility for managing MySQL databases through dynamic SQL. It simplifies database setup and provides convenient methods for creating tables, inserting data, and running queries, all from user-provided SQL strings.

## Features
- Connects and selects MySQL databases automatically
- Validates and executes SQL commands (`CREATE`, `INSERT`, `SELECT`)
- Minimal, extendable, and beginner-friendly

## Usage
```python
from database import Database


db = Database(
    dbname="DatabaseName",
    host="localhost",     #  Your MySQL host (default is localhost)
    user="root",          # Your MySQL username (default is root)
    password="your_password_here"  # your MySQL password
)

db.create_table("CREATE TABLE IF NOT EXISTS users (id INT, name VARCHAR(100));")
db.insert_into("INSERT INTO users (id, name) VALUES (1, 'Isreal');")
db.query("SELECT * FROM users;")