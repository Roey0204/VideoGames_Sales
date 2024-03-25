import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = "C:/Data-Analysis/Dataset/vgchartz-2024.csv"
df = pd.read_csv(path)

top_selling_games = df.groupby('title')['total_sales'].sum().sort_values(ascending=False).head(10)

# Define a color palette
colors = plt.cm.tab10(np.arange(len(top_selling_games)))

plt.figure(figsize=(8,6))
bars = plt.bar(top_selling_games.index, top_selling_games.values, color=colors)


for bar, value in zip(bars, top_selling_games.values):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{value:.0f}M', 
             ha='center', va='bottom', fontsize=8)
    
plt.title("Top Sales")
plt.xlabel("Games")
plt.ylabel("Total Sales (M)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
