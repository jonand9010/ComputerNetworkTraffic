#%%
import pandas as pd
import pathlib
import networkx as nx
from networkx.algorithms.centrality import degree_centrality
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib import animation
from utils.network_utils import *
#%%

#%%

path = pathlib.Path(__file__).parent.resolve()

df = pd.read_csv(str(path) + '/cs448b_ipasn.csv')

dates = df['date'].unique()

network = Network()
network.build_network(df)



#%%
from networkx.drawing.nx_pylab import draw_networkx_nodes, draw_networkx_edges





#%%


#node_colors = [network.nodes[i]['color'] for i in range(network.number_of_nodes)]
node_colors = [network.nodes[node].get('color') for node in network.nodes()]
test_colors = [network[u][v]['color'] for u,v in network.edges()]


fig = plt.figure()
ax = plt.axes()



pos=nx.spring_layout(network)

network.__dict__.update({'pos': pos})
draw_networkx_nodes(network, ax = ax, pos = network.pos, node_size = network.node_sizes, node_color = node_colors)
draw_networkx_edges(network, ax = ax, pos = network.pos, alpha = 0.1, edge_color = test_colors)

T = len(dates)

for i in range(T):
    plt.cla()

    network.color_network_nodes(network.dates[i])
    network.color_network_edges(network.dates[i])

    node_colors = [network.nodes[node].get('color') for node in network.nodes()]
    edge_colors = [network[u][v]['color'] for u,v in network.edges()]


    draw_networkx_nodes(network, ax = ax, pos = network.pos, node_size = network.node_sizes, node_color = node_colors)
    draw_networkx_edges(network, ax = ax, pos = network.pos, alpha = 0.5, edge_color = edge_colors)

    if dates[i] in ['2006-08-24', '2006-09-04', '2006-09-18', '2006-09-26']: 
        plt.title('Date: ' + dates[i], color = 'r')
    else:
        plt.title('Date: ' + dates[i], color = 'k')
    plt.pause(0.1)


plt.show()
