import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pylab import draw_networkx_nodes, draw_networkx_edges
from utils.network_utils import *

def plot_timeline(network, time_period, dates, suspected_dates = []):

    fig = plt.figure()
    ax = plt.axes()

    pos=nx.spring_layout(network)

    network.__dict__.update({'pos': pos}) 

    for i in range(time_period):
        plt.cla()

        network.color_network_nodes(network.dates[i])
        network.color_network_edges(network.dates[i])

        network.__dict__.update({'node_colors': [network.nodes[node].get('color') for node in network.nodes()],
                    'edge_colors': [network[u][v]['color'] for u,v in network.edges()],
                    'edge_width': [network[u][v]['width'] for u,v in network.edges()]})

        draw_networkx_nodes(network, ax = ax, pos = network.pos, node_size = network.node_sizes, node_color = network.node_colors)
        draw_networkx_edges(network, ax = ax, pos = network.pos, width = network.edge_width, edge_color = network.edge_colors)

        if dates[i] in suspected_dates: 
            plt.title('Date: ' + dates[i], color = 'r')
        else:
            plt.title('Date: ' + dates[i], color = 'k')
        plt.pause(0.1)


    plt.show()