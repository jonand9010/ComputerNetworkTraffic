import networkx as nx
import numpy as np 
import pandas as pd

class Network(nx.Graph):
    def __init__(self ): 
        super().__init__()
       

    def build_network(self, df, colors = ['red', 'black']):
        self.df = df
        self.node_list = np.concatenate(( self.df['l_ipn'].unique(), self.df['r_asn'].unique()))
        self.node_list = np.unique(self.node_list, axis = 0)
        self.number_of_nodes = len(self.node_list)
        self.number_of_edges = len(self.df['l_ipn'])
        self.dates = self.df['date'].unique()
        
        self.define_edges()
        self.node_colors = []
        self.edge_colors = []
        self.node_sizes = []

        self.define_nodes(colors)

    def define_nodes(self, colors = ['black', 'red']):

        for node in range(self.number_of_nodes):

            self.add_node(self.node_list[node], name = 'node'+str(node), color = colors[0])
            self.node_sizes.append(10)

            if node in self.df['l_ipn'].values:
                
                self.nodes[node]['color'] = colors[1]

            
        
        

    def define_edges(self):
        for i in range(self.number_of_edges):

            self.add_edge(self.df['l_ipn'].values[i], self.df['r_asn'].values[i], color = 'black')

    def color_network_nodes(self, date):
        df_filtered = self.df[self.df['date'] == date]
        for node in self.node_list:

            self.nodes[node]['color'] = 'black'
            if node in df_filtered['r_asn'].values:
                self.nodes[node]['color'] = 'blue'


    def color_network_edges(self, date):

        self.define_edges()
        df_filtered = self.df[self.df['date'] == date]

        for edge in df_filtered.index:

            node1, node2 = df_filtered['l_ipn'][edge], df_filtered['r_asn'][edge]

            self[node1][node2]['color'] = 'red'

