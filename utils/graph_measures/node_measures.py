import pandas as pd
import networkx as nx 

class NodeMeasures:

    def __init__(self, network):
        self.network = network
        self.initiate_results()
        self.temp_data_dict = {}

    def initiate_results(self):
        columns = [node for node in self.network.nodes ]
        columns.append('measure')
        self.results = pd.DataFrame(columns = columns)

    def append_result(self):
        self.temp_data_dict.update({'measure': self.measure})
        self.results = self.results.append(self.temp_data_dict, ignore_index = True)
        self.temp_data_dict = {}

    def clear_results(self):
        self.initiate_results()


class DegreeCentrality(NodeMeasures):
    
    def __init__(self, network):
        super().__init__(network)
        self.measure = 'DegreeCentrality'
   

    def compute_measure(self, **kwargs):
        self.temp_data_dict.update(nx.degree_centrality(self.network))
        self.temp_data_dict.update(kwargs)
        self.append_result()


class BetweennessCentrality(NodeMeasures):

    def __init__(self, network):
        super().__init__(network)
        self.measure = 'BetweennessCentrality'

    def compute_measure(self, **kwargs):

        self.temp_data_dict = nx.betweenness_centrality(self.network)
        self.temp_data_dict.update(kwargs)
        self.append_result()