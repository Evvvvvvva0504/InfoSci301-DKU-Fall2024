import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm
from adjustText import adjust_text  # For preventing label overlap
'''
data:https://github.com/jpatokal/openflights/blob/master/data/routes.dat
'''
# Define the column names based on the structure
columns = [
    "Airline_Code", "Flight_Number", "Source_Airport", "Source_Airport_ID",
    "Destination_Airport", "Destination_Airport_ID", "Codeshare", "Stops", "Equipment"
]

# Load the data
file_path = "routes.dat"  # Replace with your actual file path
routes_df = pd.read_csv(file_path, header=None, names=columns)
routes_df = routes_df.head(2000)
# Display the first few rows
print("Data preview:")
print(routes_df.head())

# Initialize a directed graph
G = nx.DiGraph()

# Add edges to the graph
for _, row in tqdm(routes_df.iterrows(), total=routes_df.shape[0], desc="Adding edges"):
    G.add_edge(row["Source_Airport"], row["Destination_Airport"], airline=row["Airline_Code"])

# Display basic information about the graph
print("\nGraph Information:")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Is the graph directed? {'Yes' if G.is_directed() else 'No'}")

# Visualization setup
plt.figure(figsize=(20, 16))  # Large figure for clarity

# Generate positions for nodes using a spring layout with increased spread
print("Calculating node positions...")
pos = nx.spring_layout(G, seed=42, k=0.15)  # Adjust the `k` parameter for better spacing

# Draw nodes
print("Drawing nodes...")
nx.draw_networkx_nodes(
    G, pos, node_color='skyblue', node_size=600, alpha=0.9
)

# Draw edges
print("Drawing edges...")
nx.draw_networkx_edges(
    G, pos, edge_color='gray', alpha=0.5, arrows=True, arrowsize=15, width=0.5
)

# Draw labels using adjustText to prevent overlap
print("Drawing labels...")
texts = []
for node, (x, y) in pos.items():
    texts.append(plt.text(x, y, node, fontsize=8, fontweight="bold", color="darkblue"))

# Use adjustText to shift overlapping labels
adjust_text(
    texts, 
    arrowprops=dict(arrowstyle='-', color='gray', lw=0.5),  # Optional arrows to connect shifted labels to nodes
)

# Title and display
plt.title("Improved Airline Routes Network", fontsize=20, fontweight='bold')
plt.axis("off")  # Turn off the axes
plt.tight_layout()
plt.savefig("output", dpi=300)

plt.show()
