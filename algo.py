import networkx as nx
import matplotlib.pyplot as plt
import random as rdm
import readFile as rf

#----------------------------------------------------------------------------------------------
#Fonction qui retourne le niveau entre deux sommets
#Input : Un graphe, le niveau initial, deux noeuds
#Output : level, le niveau entre deux sommets
def count_level(G, level, node1, node2):
    level = G.number_of_edges(node1, node2)

    return level
#----------------------------------------------------------------------------------------------