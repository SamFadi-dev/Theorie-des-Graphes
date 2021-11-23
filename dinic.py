import readFile as rf
import networkx as nx
import matplotlib.pyplot as plt
import generate as gn

G = rf.read_create("graphe.txt")

rf.windowed_graph(G)

          