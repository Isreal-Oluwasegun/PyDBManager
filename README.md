# PyDBManager

**PyDBManager** is a lightweight Python utility for managing MySQL databases through dynamic SQL. It simplifies database setup and provides convenient methods for creating tables, inserting data, and running queries, all from user-provided SQL strings.

## Features
- Connects and selects MySQL databases automatically
- Validates and executes SQL commands (`CREATE`, `INSERT`, `SELECT`)
- Minimal, extendable, and beginner-friendly

## Usage
```python
from pydbmanager import Database

db = Database("MyDatabase")
db.create_table("CREATE TABLE IF NOT EXISTS users (id INT, name VARCHAR(100));")
db.insert_into("INSERT INTO users (id, name) VALUES (1, 'Isreal');")
db.query("SELECT * FROM users;")
