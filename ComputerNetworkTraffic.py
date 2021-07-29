#%%
import pandas as pd
import pathlib
import networkx as nx
from networkx.algorithms.centrality import degree_centrality
import numpy as np
from utils.network_utils import *

#%%

path = pathlib.Path(__file__).parent.resolve()

df = pd.read_csv(str(path) + '/cs448b_ipasn.csv')

dates = df['date'].unique()

network = Network()
network.build_network(df)



#%%
from networkx.drawing.nx_pylab import draw_networkx_nodes, draw_networkx_edges
from utils.plot_network_activity import plot_timeline

timeperiod = len(dates)

suspected_dates = ['2006-08-24', '2006-09-04', '2006-09-18', '2006-09-26']

plot_timeline(network, timeperiod, dates, suspected_dates)



