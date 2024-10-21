import matplotlib.pyplot as plt

# Data for cheesecake flavors and their sales numbers
flavors = ['Classic', 'Strawberry', 'Chocolate', 'Cherry', 'Keylime', 'Oreo']
sales = [350, 220, 180, 190, 160, 210]

# Create a bar chart for cheesecake flavors
fig, ax = plt.subplots()

# Plot the bar chart matching the colors for each flavor of cheesecakr
colors = ['#E6DDD8', '#FF69B4', '#8B4513', '#800000', '#B9FF66', '#000000']
ax.bar(flavors, sales, color=colors)

# Set the chart title and labels
ax.set_title('Cheesecake Sales by Flavor', fontsize=22)
ax.set_xlabel('Flavor', fontsize=18)
ax.set_ylabel('Number of Cheesecakes Sold', fontsize=18)

# I added gridlines so it can be easier to read 
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Customize the tick labels
ax.tick_params(axis='both', labelsize=25)

# Display the plot
plt.show()
