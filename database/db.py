import sqlite3

conn = sqlite3.connect('roadwatch.db')

cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS complaints(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_name TEXT,
    damage_type TEXT,
    severity TEXT,
    status TEXT,
    date_time TEXT
)
''')

print("Table created successfully")

conn.commit()
conn.close()