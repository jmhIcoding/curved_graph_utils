__author__ = 'jmh081701'
import matplotlib.pyplot as plt
import numpy as np
import bezier
from matplotlib.collections import LineCollection
import networkx as nx
import random

G = nx.Graph()
G.add_node(0,burst_id =0)
G.add_node(1,burst_id =1)
G.add_node(2,burst_id =1)
G.add_node(3,burst_id =2)
G.add_node(4, burst_id=1)

G.add_edge(0,1)

G.add_edge(1,2)

G.add_edge(0,4)
G.add_edge(1,3)

G.add_edge(2,4)
G.add_edge(1,4)
graph = G
def curved_line(x0, y0, x1, y1, eps=0.2, pointn=30, distance=1):

    x2 = (x0+x1)/2.0 + 0.3 ** (eps+abs(x0-x1)) * (-1) ** distance
    y2 = (y0+y1)/2.0 + 0.2 ** (eps+abs(y0-y1)) * (-1) ** distance
    nodes = np.asfortranarray([
        [x0, x2, x1],
        [y0, y2, y1]
    ])
    curve = bezier.Curve(nodes,
                         degree=2)
    s_vals = np.linspace(0.0, 1.0, pointn)
    data=curve.evaluate_multi(s_vals)
    x=data[0]
    y=data[1]
    segments =[]
    for index in range(0,len(x)):
        segments.append([x[index],y[index]])
    segments = [segments]
    return  segments
def curved_graph(_graph, pos = None, eps=0.2, pointn=30):

    if pos == None:
        pos = nx.spring_layout(graph)

    for u,v in graph.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        segs = curved_line(x0,y0,x1,y1,distance=abs(u-v))
        lc = LineCollection(segs)
        plt.gca().add_collection(lc)
        plt.gca().autoscale_view()

def burst_layout(_graph):
    burst_dict = {}
    ##找出burst, 以及对应的节点
    for node in graph.nodes():

        burst_id =  graph.nodes[node]['burst_id']
        if burst_id not in burst_dict:
            burst_dict[burst_id] = [node]
        else:
            burst_dict[burst_id].append(node)
    max_burst = max([len(burst_dict[x]) for x in burst_dict])
    burst_num = len(burst_dict)
    pos = {}
    xs = np.linspace(0, 2 * burst_num,num=burst_num)
    burst_pos = { }
    for burst in burst_dict:
        burst_pos[burst] = np.linspace(0, 2 * max_burst ,num= len(burst_dict[burst])+2)[1:-1]
    for node in graph.nodes():
        burst_index = burst_dict[graph.nodes[node]['burst_id']].index(node)
        pos[node]=[xs[graph.nodes[node]['burst_id']], burst_pos[graph.nodes[node]['burst_id']][burst_index]]

    return pos
if __name__ == '__main__':
    #画节点
    pos =  burst_layout(graph)
    print(pos)
    labels={}
    for each in graph.nodes():
        labels[each] = str(graph.nodes[each]['burst_id']) +'->' + str(each)
    #nx.draw(graph,pos,with_labels=False)
    nx.draw_networkx_nodes(graph,pos)

    #画标签
    nx.draw_networkx_labels(graph, pos, labels=labels)

    #画曲线

    curved_graph(graph,pos)

    plt.show()

