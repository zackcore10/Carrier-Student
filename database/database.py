import sqlite3

connection = sqlite3.connect("careerai.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    programming TEXT,
    math TEXT,
    communication TEXT,
    interest TEXT,
    experience TEXT,
    recommended_career TEXT
)
""")

connection.commit()

connection.close()

print("Database created successfully!")