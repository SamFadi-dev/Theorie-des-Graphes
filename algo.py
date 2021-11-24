import networkx as nx
import matplotlib.pyplot as plt
import random as rdm
import readFile as rf

#----------------------------------------------------------------------------------------------
#Fonction qui retourne le niveau entre deux sommets
#Input : Un graphe G, le niveau initial level, deux noeuds node1 et node2
#Output : level, le niveau entre deux sommets
def count_level(G, level, node1, node2):
    level = G.number_of_edges(node1, node2)

    return level

#----------------------------------------------------------------------------------------------
#Fonction qui retourne la source et le puit
#Input : Un graphe G
#Output : la source et le puit, source | sink
def source_sink (G):
    nodes = list(G.nodes)
    source = nodes[0]
    sink = nodes[len(nodes)-1]

    return (source, sink)

#----------------------------------------------------------------------------------------------
#Fonction qui retourne la plus petite capacité dans un graphe
#Input : Un graphe G
#Output : Capacité minimum | minCap
def min_cap(G):
    capacityList = []
    for edge in G:
        edgeDic = G.get_edge_data(edge)
        capacityList.append(edge['capacity'])

    for i in range (0, len(capacityList)):
        if(capacityList[0] < capacityList[i]):
            minCap = capacityList[i]


    return minCap

#----------------------------------------------------------------------------------------------
#Fonction qui retourne le flow maximum
#Input : un entier minCap représentant la capacité minimale
#Output : Le flow maximum | maxFlow
def max_flow(minCap):
    maxFlow = 0
    maxFlow = maxFlow + minCap

    return maxFlow