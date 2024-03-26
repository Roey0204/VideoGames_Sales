import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the dataset
path = "C:/Data-Analysis/Video_Game_Sales/Dataset/vgchartz-2024.csv"
df = pd.read_csv(path)

# Group the data by game title and console, then sum up the total sales and get the top 10 selling games
platforms = df.groupby(['title', 'console'])['total_sales'].sum().sort_values(ascending=False).head(10)

# Extract titles, consoles, and sales values from the grouped data
titles = [index[0] for index in platforms.index]
consoles = [index[1] for index in platforms.index]
sales = platforms.values

# Get unique consoles and assign colors to them
unique_consoles = np.unique(consoles)
colors = plt.cm.tab20(np.linspace(0, 1, len(unique_consoles)))
console_colors = dict(zip(unique_consoles, colors))

# Convert sales to millions (currently not used in this code)
sales_in_millions = sales  # dividing by 1 million to get the values in millions
#sales_in_millions = sales / 1e6  # dividing by 1 million to get the values in millions

# Create a figure for the plot
plt.figure(figsize=(14, 10))

# Dictionary to keep track of added consoles to legend
legend_added = {}

# Iterate through the top-selling games
for i in range(len(titles)):
    console = consoles[i]
    color = console_colors[console]
    
    # Check if console is not already added to legend
    if console not in legend_added:
        # Plot the bar with console label
        plt.bar(titles[i], sales_in_millions[i], color=color, label=console)
        legend_added[console] = True  # Mark console as added to legend
    else:
        # Plot the bar without label if already added to legend
        plt.bar(titles[i], sales_in_millions[i], color=color)

# Set plot labels and title
plt.xlabel('Game Titles')
plt.ylabel('Sales (Millions)')
plt.title('Top Selling Games by Platform')
plt.xticks(rotation=45, ha='right')

# Add legend with unique console entries
handles, labels = plt.gca().get_legend_handles_labels()
unique_labels = []
unique_handles = []
for handle, label in zip(handles, labels):
    if label not in unique_labels:
        unique_labels.append(label)
        unique_handles.append(handle)
plt.legend(unique_handles, unique_labels, title='Console', loc='best')

# Add "Millions" to y-axis tick labels
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}M'))

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
