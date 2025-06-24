import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the transformed data
df = pd.read_csv('transformed/transformed_full.csv')

# 1. Bar plot: Number of orders per region
plt.figure(figsize=(8, 5))
df['region'].value_counts().plot(kind='bar', color='teal', edgecolor='black')
plt.title('Number of Orders per Region')
plt.xlabel('Region')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.savefig('transformed/bar_orders_per_region.png')
plt.close()

# 2. Boxplot: Total Price by Product (only non-null total_price)
plt.figure(figsize=(10, 6))
sns.boxplot(x='product', y='total_price', data=df[df['total_price'].notnull()], palette='Set2')
plt.title('Total Price Distribution by Product')
plt.xlabel('Product')
plt.ylabel('Total Price')
plt.tight_layout()
plt.savefig('transformed/box_total_price_by_product.png')
plt.close()

# 3. Line plot: Number of Orders per Month (order_month)
plt.figure(figsize=(8, 5))
order_counts = df['order_month'].value_counts().sort_index()
plt.plot(order_counts.index, order_counts.values, marker='o', linestyle='-', color='purple')
plt.title('Number of Orders per Month')
plt.xlabel('Order Month')
plt.ylabel('Number of Orders')
plt.xticks(order_counts.index)
plt.tight_layout()
plt.savefig('transformed/line_orders_per_month.png')
plt.close()

print('Three unique visualizations have been saved in the transformed/ directory.') 