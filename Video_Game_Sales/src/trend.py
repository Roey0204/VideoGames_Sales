import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
path = "C:/Data-Analysis/Video_Game_Sales/Dataset/vgchartz-2024.csv"
df = pd.read_csv(path)

threshold_release_year = 2010

df['release_date'] = pd.to_datetime(df['release_date'])
df['platform_category'] = np.where(df['release_date'].dt.year < threshold_release_year, 'Older', 'Newer')
sales_trends = df.groupby(['platform_category', df['release_date'].dt.year])['total_sales'].sum().reset_index()

plt.figure(figsize=(12, 8))

# Plotting the lines for 'Older' and 'Newer' platform categories
for category in sales_trends['platform_category'].unique():
    category_data = sales_trends[sales_trends['platform_category'] == category]
    plt.plot(category_data['release_date'], category_data['total_sales'], marker='o', label=category)

plt.title('Sales Trends Between Older and Newer Platforms')
plt.xlabel('Release Year')
plt.ylabel('Total Sales')
plt.legend(title='Platform Category')
plt.tight_layout()
plt.show()
