import networkx as nx
import matplotlib.pyplot as plt
import random as rdm
import readFile as rf

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

#----------------------------------------------------------------------------------------------
#Fonction qui retourne le niveau d'un sommet
#Input : Un graphe, une source et un sommet cible | G source target
#Output : Le niveau du sommet | level
def find_level (G, source, target):
    array = 0
    for i in range(1, int(target)+1):
        array = nx.shortest_path(G, source, str(i))

    level = int(len(array))

    #Si un arc, on ajoute un niveau pour contre-balancer le return
    if(level == 1):
            level = level + 1

    return level-1

#----------------------------------------------------------------------------------------------
#Fonction qui retourne le niveau des sommets
#Input : Un graphe | G 
#Output : Le niveau des sommets modifié
def all_levels (G):
    numberN = nx.number_of_nodes(G)
    allnodes = list(G.nodes)
    source, sink = source_sink(G)

    G.nodes["1"]["level"] = 0
    G.nodes[sink]

    for i in range(2, numberN+1):
        level = find_level(G, source, str(i))
        
        if(("level" in G[str(i)]) == False):
            G.nodes[str(i)]["level"] = level
        
#----------------------------------------------------------------------------------------------
def augmenting_level_path (G):
    source, sink = source_sink(G)
    paths = list(nx.shortest_simple_paths(G, source, sink))
    print(paths)

    #Parcourir la liste de chemins
    for i in range(len(paths)):
        count = 0
        #Parcourir un chemin sommet par sommet
        for j in range(len(paths[i])):
            #Si le dernier sommet est atteint, on renvoit ce chemin et True
            if(count == len(paths[i])-1):
                return paths[i]
            #Si dernier sommet, ne rien faire
            if(i+1 != len(paths[i])):
                #Si le niveau d'après est plus petit, on arrête la boucle
                node1 = G.nodes[str(i+1)]["level"]
                node2 = G.nodes[str(i+2)]["level"]
                if (node1 >= node2):
                    print("lol")
                    break
                else:
                    count = count + 1
    #Si rien n'a été trouvé, on retourne False
    return paths[i]

#----------------------------------------------------------------------------------------------
def check_augmenting_level_path(G):
    path = augmenting_level_path(G)

    if(path):
        return True
    else:
        return False
            
#----------------------------------------------------------------------------------------------
def check_flow(G, path):
    for i in range(len(path)-1):
        if G.get_edge_data(str(i+1), str(i+2), "capacity")["capacity"] > 0:
             pass
        else:
            return False

    return True







    









