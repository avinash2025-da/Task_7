# Task 7: Sales Summary using Python and SQLite

##Objective
To extract and summarize basic sales information from a SQLite database using SQL inside Python and visualize the output using a bar chart.

##Tools Used
- **Python** (Core language)
- **SQLite3** (Database engine)
- **Pandas** (Data manipulation)
- **Matplotlib** (Data visualization)

##Files Included
- `task7_sales_summary.py`: Python script that performs the complete task.
- `sales_data.db`: SQLite database with sample sales data.
- `sales_chart.png`: Bar chart showing revenue by product.

##Dataset
A sample sales table was created manually with the following columns:
- `invoice_id`
- `product`
- `category`
- `quantity`
- `price`
- `customer_name`
- `city`
- `date`

The records include Indian brands, cities, and customer names for realism.

##SQL Query Used
```sql
SELECT product, SUM(quantity) AS total_qty, 
       ROUND(SUM(quantity * price), 2) AS revenue 
FROM sales 
GROUP BY product
ORDER BY revenue DESC;
```
##Output
- Total Quantity Sold by Product
- Total Revenue Generated
- Revenue Visualized using a Bar Chart

---
