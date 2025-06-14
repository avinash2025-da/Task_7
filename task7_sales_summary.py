
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to SQLite database (or create it if not exists)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Step 2: Create the sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    invoice_id TEXT,
    product TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL,
    customer_name TEXT,
    city TEXT,
    date TEXT
)
''')

# Step 3: Insert sample sales data with Indian names and cities
sample_data = [
    ('INV001', 'Parle-G', 'Biscuits', 20, 5.0, 'Ravi Sharma', 'Delhi', '2025-06-01'),
    ('INV002', 'Dairy Milk', 'Chocolate', 15, 10.0, 'Anjali Verma', 'Mumbai', '2025-06-02'),
    ('INV003', 'Maggi', 'Noodles', 10, 12.0, 'Kiran Kumar', 'Hyderabad', '2025-06-03'),
    ('INV004', 'Lays', 'Snacks', 25, 10.0, 'Priya Singh', 'Bengaluru', '2025-06-04'),
    ('INV005', 'Good Day', 'Biscuits', 30, 6.0, 'Vikram Joshi', 'Ahmedabad', '2025-06-05'),
    ('INV006', 'Coca Cola', 'Beverages', 18, 35.0, 'Sonal Mehta', 'Pune', '2025-06-06'),
    ('INV007', 'Red Bull', 'Beverages', 5, 120.0, 'Amitabh Rao', 'Chennai', '2025-06-07'),
    ('INV008', 'Kurkure', 'Snacks', 20, 8.0, 'Meena Rathi', 'Kolkata', '2025-06-08'),
    ('INV009', 'Frooti', 'Beverages', 22, 25.0, 'Rohit Nair', 'Thiruvananthapuram', '2025-06-09'),
    ('INV010', 'Perk', 'Chocolate', 12, 7.0, 'Lakshmi Iyer', 'Visakhapatnam', '2025-06-10'),
    ('INV011', 'Sprite', 'Beverages', 14, 30.0, 'Harshita Rao', 'Nagpur', '2025-06-11'),
    ('INV012', 'Hide & Seek', 'Biscuits', 16, 7.0, 'Neeraj Bansal', 'Lucknow', '2025-06-12'),
    ('INV013', 'Thumbs Up', 'Beverages', 10, 35.0, 'Deepika Agarwal', 'Kanpur', '2025-06-13'),
    ('INV014', '5 Star', 'Chocolate', 13, 9.0, 'Arjun Desai', 'Surat', '2025-06-14'),
    ('INV015', 'Treat', 'Biscuits', 18, 6.0, 'Kavita Shetty', 'Coimbatore', '2025-06-15')
]
cursor.executemany('INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?, ?, ?)', sample_data)
conn.commit()

# Step 4: SQL query to get total quantity and revenue by product
query = '''
SELECT product, SUM(quantity) AS total_qty, 
       ROUND(SUM(quantity * price), 2) AS revenue 
FROM sales 
GROUP BY product
ORDER BY revenue DESC
'''
df = pd.read_sql_query(query, conn)

# Step 5: Display the results
print("SALES SUMMARY:")
print(df)

# Step 6: Plot bar chart for revenue
plt.figure(figsize=(12, 6))
df.plot(kind='bar', x='product', y='revenue', legend=False, color='green')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Close connection
conn.close()
