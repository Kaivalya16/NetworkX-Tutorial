import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

edges = [(1,2), (2,3), (3, 4), (2, 4), (4, 1)]

g = nx.Graph()  # Simple Un-Directed Graph

# adding edges through edge list
g2 = nx.from_edgelist(edges) # creating a new graph through edges list
g.add_edges_from(edges) # add edges to a graph

# Adjacency Matrix
print(nx.adjacency_matrix(g2))

twod_array = np.array([[0, 1, 0],
                       [1, 1, 1],
                       [0, 0, 0]])
g3 = nx.from_numpy_array(twod_array)


# Complete Graphs
# g4 = nx.complete_graph(4)
g4 = nx.complete_graph(5) #--> planar graph is not possible when graph is Complete





'''
g.add_edge(1, 2) # edge b/w node 1 and 2
g.add_edge(2, 3, weight=9) # edge b/w 2 and 3 with weight 9
g.add_edge("A", "B")
g.add_edge("B", "B")

g.add_node("C")
g.add_node(print) # adding built-in print fuunction as node
'''

nx.draw_spring(g4, with_labels=True)
plt.show()

# nx.draw_circular(g, with_labels=True)
# plt.show()

# nx.draw_shell(g, with_labels=True)
# plt.show()

# nx.draw_spectral(g, with_labels=True)
# plt.show()

# nx.draw_random(g, with_labels=True)
# plt.show()

nx.draw_planar(g4, with_labels=True) # no edge crosses another edge
plt.show()

# g_2 = nx.DiGraph() # Simple Directed Graph
# g_3 = nx.MultiGraph() # Graphs with Multi-edges b/w 2 nodes
# g_4 = nx.MultiDiGraph() # Directed version of MultiGraph
