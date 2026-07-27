import re
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
username = input("Enter username: ")


pattern = r"^[A-Za-z0-9_-]{3,20}$"

if not re.fullmatch(pattern, username):
    print("Invalid username.")
else:
    cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    ) 