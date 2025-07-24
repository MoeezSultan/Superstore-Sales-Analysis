import pandas as pd

df = pd.read_csv(r'C:\Users\HP user\Desktop\Data Science\python\Super Market\Sample - Superstore.csv', encoding='latin1')

print(df.head())
  
print(df.columns)

print(df.isnull().sum())

print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("TOTAL SALES:",df['Sales'].sum())

#What are the monthly/yearly sales trends?
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()
print(monthly_sales)    

import matplotlib.pyplot as plt

# Optional: Create a 'Year-Month' column for better x-axis labels
monthly_sales['Year_Month'] = monthly_sales['Year'].astype(str) + '-' + monthly_sales['Month'].astype(str).str.zfill(2)

# Plotting
plt.figure(figsize=(14, 6))
plt.plot(monthly_sales['Year_Month'], monthly_sales['Sales'], marker='o', linestyle='-')

plt.title('Monthly Sales Trend')
plt.xlabel('Year-Month')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Which region/city has the highest sales?
df['Region'] = df['Region'].str.strip()
region_sales = df.groupby('Region')['Sales'].sum().reset_index()
print(region_sales)


# Which product or category is the top seller?
product_sales = df.groupby('Product Name')['Sales'].sum().reset_index()
print(product_sales)
top_product = product_sales.sort_values(by='Sales', ascending=False).head(1)
print("Top Selling Product:")
print(top_product)


# What is the average order value (AOV)?
average_order_value = df['Sales'].mean()
print("Average Order Value (AOV):", average_order_value)


# 📌 Customer Behavior (if customer data exists)
# How many unique customers are there?
unique_customers = df['Customer ID'].nunique()
print("Unique Customers:", unique_customers)


# Which customers have made the most purchases?
top_customers = df.groupby('Customer ID')['Sales'].sum().reset_index()
top_customers = top_customers.sort_values(by='Sales', ascending=False).head(10)
print("Top Customers by Sales:")
print(top_customers)

#  1. Total Sales by Region (Horizontal Bar Chart)
region_sales = df.groupby('Region')['Sales'].sum().sort_values()
plt.figure(figsize=(8, 5))
plt.barh(region_sales.index, region_sales.values, color='skyblue')
plt.title('Total Sales by Region')
plt.xlabel('Sales')
plt.tight_layout()
plt.show()

# 2. Sales by Category / Sub-Category (Bar Chart)
# Category
cat_sales = df.groupby('Category')['Sales'].sum()
plt.figure(figsize=(6, 4))
plt.bar(cat_sales.index, cat_sales.values, color='orange')
plt.title('Sales by Category')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# Sub-Category
subcat_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values()
plt.figure(figsize=(10, 6))
plt.barh(subcat_sales.index, subcat_sales.values, color='green')
plt.title('Sales by Sub-Category')
plt.xlabel('Sales')
plt.tight_layout()
plt.show()

# 3. Top 10 Selling Products (Bar Chart)
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
plt.bar(top_products.index, top_products.values, color='purple')
plt.title('Top 10 Products by Sales')
plt.ylabel('Sales')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# 5. Sales Share by Region (Pie Chart)
region_sales = df.groupby('Region')['Sales'].sum()
plt.figure(figsize=(6, 6))
plt.pie(region_sales.values, labels=region_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('Sales Share by Region')
plt.tight_layout()
plt.show()

# 6. Discount vs Profit (Scatter Plot)
plt.figure(figsize=(8, 5))
plt.scatter(df['Discount'], df['Profit'], alpha=0.5, color='red')
plt.title('Discount vs Profit')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.grid(True)
plt.tight_layout()
plt.show()

# 7. Profit by Region (Bar Chart)
region_profit = df.groupby('Region')['Profit'].sum()
plt.figure(figsize=(6, 4))
plt.bar(region_profit.index, region_profit.values, color='teal')
plt.title('Profit by Region')
plt.ylabel('Profit')
plt.tight_layout()
plt.show()

# 8. Profit Distribution by Segment (Box Plot using matplotlib)
segments = df['Segment'].unique()
data_to_plot = [df[df['Segment'] == seg]['Profit'].values for seg in segments]

plt.figure(figsize=(6, 4))
plt.boxplot(data_to_plot, labels=segments)
plt.title('Profit Distribution by Segment')
plt.ylabel('Profit')
plt.grid(True)
plt.tight_layout()
plt.show()

# 9. Heatmap (Manually using matplotlib imshow)
heat_data = df.pivot_table(index='Sub-Category', columns='Region', values='Profit', aggfunc='sum')
plt.figure(figsize=(10, 6))
plt.imshow(heat_data, cmap='YlGnBu', aspect='auto')
plt.colorbar(label='Profit')
plt.xticks(ticks=range(len(heat_data.columns)), labels=heat_data.columns)
plt.yticks(ticks=range(len(heat_data.index)), labels=heat_data.index)
plt.title('Profit Heatmap (Sub-Category vs Region)')
plt.tight_layout()
plt.show()


# 10. Top 10 Customers by Sales (Bar Chart)
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
plt.bar(top_customers.index, top_customers.values, color='steelblue')
plt.title('Top 10 Customers by Sales')
plt.ylabel('Sales')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


