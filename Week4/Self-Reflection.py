import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Initialize the figure
fig, ax = plt.subplots(figsize=(12, 12))

# Draw Kunshan as the central focus
kunshan_circle = patches.Circle((0, 0), 0.5, color='blue', alpha=0.6, label="Kunshan")
ax.add_patch(kunshan_circle)
plt.text(0, 0, "Kunshan", color='white', ha='center', va='center', fontsize=10)

# Add surrounding cities
cities = {
    "Nanjing": (-4, 3),
    "Suzhou": (-2, 0),
    "Shanghai": (3, -1),
    "Hangzhou": (-2.5, -3),
    "Kunshan Airport": (2.5, 2),
    "Kunshan Port": (1, -3)
}
city_colors = {
    "Nanjing": "yellow",
    "Suzhou": "orange",
    "Shanghai": "orange",
    "Hangzhou": "yellow",
    "Kunshan Airport": "cyan",
    "Kunshan Port": "cyan"
}

# Add roads
roads = {
    "Highway A": (-2, -1.5),
    "Highway B": (1.5, 0.5),
}

# Draw connections (highways, railways, airport, and port links)
connections = [
    ((0, 0), (-4, 3)),  # Kunshan to Nanjing
    ((0, 0), (-2, 0)),  # Kunshan to Suzhou
    ((0, 0), (3, -1)),  # Kunshan to Shanghai
    ((0, 0), (-2.5, -3)),  # Kunshan to Hangzhou
    # ((0, 0), (2.5, 2)),  # Kunshan to Kunshan Airport
    # ((0, 0), (1, -3)),  # Kunshan to Kunshan Port
    ((0, 0), (-2, -1.5)),  # Kunshan to Highway A
    ((0, 0), (1.5, 0.5)),  # Kunshan to Highway B
]

for start, end in connections:
    ax.plot([start[0], end[0]], [start[1], end[1]], color='gray', linestyle='--', alpha=0.7)
    ax.annotate("", xy=end, xytext=start, arrowprops=dict(arrowstyle="->", color='black', lw=1.5))

# Plot city markers and labels
for city, (x, y) in cities.items():
    ax.scatter(x, y, color=city_colors[city], s=100, label=city)
    plt.text(x, y, city, color='black', fontsize=9, ha='center', va='center')

# Add roads as nodes
for road, (x, y) in roads.items():
    ax.scatter(x, y, color='green', s=80, label=road)
    plt.text(x, y, road, color='black', fontsize=9, ha='center', va='center')

# Highlight Taihu Lake
lake_x = np.array([-3, -3.5, -4, -4.5, -4.3, -3.8, -3.2])  # Approximation of lake shape
lake_y = np.array([0.5, 0, -0.5, -1, -1.5, -1.2, -0.8])
ax.fill(lake_x, lake_y, color='lightblue', alpha=0.5, label="Taihu Lake")

# Add title and legend
plt.title("Kunshan Connectivity Map", fontsize=14)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal', adjustable='datalim')
plt.axis('off')
plt.legend(loc='upper right')
plt.show()
