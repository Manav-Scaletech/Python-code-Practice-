# import re
# import sqlite3

# conn = sqlite3.connect("database.db")
# cursor = conn.cursor()
# username = input("Enter username: ")


# pattern = r"^[A-Za-z0-9_-]{3,20}$"

# if not re.fullmatch(pattern, username):
#     print("Invalid username.")
# else:
#     cursor.execute(
#         "SELECT * FROM users WHERE username = ?",
#         (username,)
#     ) 


import sqlite3

# Connect to database (or create an in-memory database)
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# Create a dummy table
cursor.execute("CREATE TABLE users (id INT, name TEXT, role TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'Alice', 'Admin'), (2, 'Bob', 'User')")

# --- PARAMETERIZED QUERY START ---
# 1. Define variables from user input
user_id = 1
user_role = "Admin"

# 2. Write the query with '?' placeholders
query = "SELECT * FROM users WHERE id = ? AND role = ?"

# 3. Pass data inside a tuple or list as the second argument
cursor.execute(query, (user_id, user_role))

# Fetch results
results = cursor.fetchall()
print(results)  # Output: [(1, 'Alice', 'Admin')]

connection.close()
