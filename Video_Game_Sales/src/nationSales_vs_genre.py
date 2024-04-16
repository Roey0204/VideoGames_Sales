import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
path = "C:/Data-Analysis/Video_Game_Sales/Dataset/vgchartz-2024.csv"
df = pd.read_csv(path)

sales_data = df[['genre', 'na_sales', 'jp_sales', 'pal_sales']]

# Melt the DataFrame to long format for easier plotting
sales_data_melted = sales_data.melt(id_vars='genre', var_name='region', value_name='sales')

# Plot grouped bar plot
plt.figure(figsize=(12, 8))

# Iterate over unique regions to plot separately
for region in sales_data_melted['region'].unique():
    region_data = sales_data_melted[sales_data_melted['region'] == region]
    plt.bar(region_data['genre'], region_data['sales'], label=region)

plt.title('Sales Distribution in North America, Japan, and PAL Regions by Genre')
plt.xlabel('Genre')
plt.ylabel('Sales')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Region', loc='upper right')
plt.tight_layout()
plt.show()