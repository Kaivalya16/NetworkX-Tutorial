import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

edges = [(1,2), (2,3), (3, 4), (3,5), (4, 6), (6,7)]

g = nx.Graph()
g.add_edges_from(edges)

g2 = nx.DiGraph()
g2.add_edges_from(edges)

# total degree of node
print(dict(g2.degree)[3]) #--> can be used in both directed or Un-directed graphs

# in-degree of node
print(dict(g2.in_degree)[3]) #--> can only use in Directed graphs

# out-degree of node
print(dict(g2.out_degree)[3]) #--> can only use in Directed graphs

# nx.draw_spring(g, with_labels=True)
# plt.show()

nx.draw_spring(g2, with_labels=True)
plt.show()

