import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths.generic import has_path
import random

co = int(input('Enter edges number :'))
source = int(1)
target = int(co)


#def count_level(level, node1, node2):
#
#    level = G.number_of_edges(node1, node2)
#
#    return level

def is_connected(co, G):
    try:
        has_path(G , 1, co)
    except:
        print("The graph is not connected \n");

def creat_graph(co):

    G = nx.DiGraph()

    for i in range(1, co, 1):
        G.add_edge(i, (random.randint(1, co)))

    is_connected(G, co)

    position = nx.random_layout(G)
    nx.draw(G, position, with_labels = True, font_weight = 'normal')
    nx.draw_networkx_edge_labels(G, position)
    plt.show()

    return G

creat_graph(co)
