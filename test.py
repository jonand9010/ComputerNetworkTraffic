from utils.networks.network import *
import networkx as nx
import matplotlib.pyplot as plt
from utils.graph_measures.node_measures import *

G = nx.Graph()

nodes = ['n1', 'n2', 'n3', 'n4']
edges = [('n1', 'n2'), ('n1', 'n3'), ('n1', 'n4'), ('n2', 'n3'), ('n2', 'n4')]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

degree_centrality = DegreeCentrality(G)
betweenness = BetweennessCentrality(G)

degree_centrality.compute_measure(G)
betweenness.compute_measure(G)
nodes = ['n1', 'n2', 'n4']
edges = [('n1', 'n2'), ('n1', 'n4'), ('n2', 'n4')]

G = nx.Graph()

G.add_nodes_from(nodes)
G.add_edges_from(edges)


degree_centrality.compute_measure(G)
betweenness.compute_measure(G)


print(degree_centrality.results)
print(betweenness.results)


#nx.draw(G, with_labels = True)
#plt.show()