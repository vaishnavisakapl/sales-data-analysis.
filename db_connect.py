import sqlite3

# Step 1: Connect to SQLite database (this will create the file if it doesn't exist)
conn = sqlite3.connect("sales_data.db")

# Step 2: Create a cursor object
cur = conn.cursor()

print("✅ Connected to SQLite database successfully!")

# Step 3: Create a simple table (optional test)
cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")
print("✅ Table created successfully!")

# Step 4: Close connection
conn.close()
print("✅ Connection closed!")
