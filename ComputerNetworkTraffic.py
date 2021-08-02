#%%
import pandas as pd
import pathlib
import networkx as nx
from networkx.algorithms.centrality import degree_centrality
import numpy as np
from utils.networks.network import *
from utils.graph_measures.node_measures import *
from utils.analysis.compile_graph_measures import CompileGraphMeasures
from tqdm import tqdm
import matplotlib.pyplot as plt
#%%

path = pathlib.Path(__file__).parent.resolve()

df = pd.read_csv(str(path) + '/datafiles/raw_cs448b_ipasn.csv')

dates = df['date'].unique()

network = Network()



degree_centrality = DegreeCentrality(network)
compiled_measures = CompileGraphMeasures(degree_centrality.results.columns.values)



for date in tqdm(dates):
    network.build_network(df[df['date']==date])
    degree_centrality.compute_measure(date = date)

   

compiled_measures.append_results(degree_centrality.results)

print(compiled_measures.dataframe)



#%%
from networkx.drawing.nx_pylab import draw_networkx_nodes, draw_networkx_edges
from utils.plot_network_activity import plot_timeline

timeperiod = len(dates)

suspected_dates = ['2006-08-24', '2006-09-04', '2006-09-18', '2006-09-26']

#plot_timeline(network, timeperiod, dates, suspected_dates)


