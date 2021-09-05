__author__ = 'jmh081701'
import networkx as nx
import random
from curved_edges import curved_edges
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
G = nx.Graph()
G.add_edge(0,1,weight=0.1)
G.add_edge(1,2,weight=0.2)
G.add_edge(0,2,weight=0.3)

pos={
    0:[1,-3],
    1:[1.1,1],
    2:[1,3],
}
nx.draw_networkx_nodes(G,pos, with_label=True)
edgewidth=[]
print(G.edges())
print(G.nodes())
for (u,v,d) in G.edges(data=True):
    edgewidth.append(round(G.get_edge_data(u,v)['weight']*10,2))
curves = curved_edges(G,pos)
print(curves)
print(curves.shape)
lc= LineCollection(curves,)

plt.gca().add_collection(lc)
plt.tick_params(axis='both',which='both',bottom=False,left=False,labelbottom=False,labelleft=False)
plt.show()
