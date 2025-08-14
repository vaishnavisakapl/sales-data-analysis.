import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect("sales_data.db")
cur = conn.cursor()
print("✅ Connected to SQLite!")

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert sample data if empty
cur.execute("SELECT COUNT(*) FROM sales")
if cur.fetchone()[0] == 0:
    data = [
        ("Apples", 10, 5.0),
        ("Apples", 15, 5.0),
        ("Bananas", 20, 2.5),
        ("Oranges", 8, 4.0),
        ("Bananas", 12, 2.5),
        ("Oranges", 10, 4.0)
    ]
    cur.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", data)
    conn.commit()
    print("✅ Sample data inserted!")

# Query with Pandas
query = """
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

print("\n📊 Sales Summary:")
print(df)

# Plot chart
df.plot(kind="bar", x="product", y="revenue", title="Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

conn.close()
