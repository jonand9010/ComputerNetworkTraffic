import pandas as pd
import networkx as nx 

class NodeMeasures:

    def __init__(self, network):
        self.network = network
        self.initiate_results()

    def initiate_results(self):
        columns = [node for node in self.network.nodes ]
        self.results = pd.DataFrame(columns = columns)

    def append_result(self, value):

        self.results = self.results = self.results.append(value, ignore_index = True)

    def clear_results(self):

        self.initiate_results()


class DegreeCentrality(NodeMeasures):
    
    def __init__(self, network):
        super().__init__(network)

    def compute_measure(self):

        degree_centrality = nx.degree_centrality(self. network)
        
        self.append_result(degree_centrality)


class BetweennessCentrality(NodeMeasures):

    def __init__(self, network):
        super().__init__(network)

    def compute_measure(self):

        betweenness_centrality = nx.betweenness_centrality(self.network)
        
        self.append_result(betweenness_centrality)