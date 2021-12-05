import networkx as nx
import matplotlib.pyplot as plt
import random as rdm
from networkx.algorithms.shortest_paths.generic import has_path
import functions as rf

#----------------------------------------------------------------------------------------------
#Fonction qui vérifié si la valeur entrée (source / puit) est correcte
#Input : Un graphe et une valeur | G, value
#Output : Booléen | True ou False
def available_value(G, value):
    tab = list(G.nodes)

    #Boucler toute la liste
    for i in range (len(tab)):
        if(value == tab[i]):
            return True

    return False

#----------------------------------------------------------------------------------------------
#Fonction qui retourne la source et le puit
#Input : Un graphe G
#Output : la source et le puit, source | sink
def source_sink (G):
    check = 0
    nodes = list(G.nodes)

    #Boucler tant qu'une source n'est pas trouvée
    while not check:
        print()
        source = str(input("Give a source : "))

        #Si sommet non dans le graphe => erreur
        if not(available_value(G, source)):
            print("Retry : not a node in the graph !")
        else:
            check = 1

    check = 0

    #Boucler tant qu'un puit n'est pas trouvé
    while not check:
        print()
        sink = str(input("Give a sink : "))

        #Si sommet non dans le graphe => erreur
        if not(available_value(G, sink)):
            print("Retry : not a node in the graph !")

        elif sink == source:
            print("Retry: same nodes !")

        else:
            check = 1

    return (source, sink)

#----------------------------------------------------------------------------------------------
#Fonction qui retourne la plus petite capacité dans un graphe
#Input : Un graphe G
#Output : Capacité minimum | minCap
def min_cap(G, path):
    list = []
    #Boucler tant que la liste est remplie
    for i in range(len(path)-1):
        #Stocker les capacités dans une liste
        edgeCap = G.get_edge_data(path[i], path[i+1], "capacity")["capacity"]
        list.append(edgeCap)

    minCap = min(list)

    return minCap

#----------------------------------------------------------------------------------------------
#Fonction qui retourne le chemin ayant un parcour avec un niveau montant
#Input : Un graphe | G 
#Output : Le chemin avec niveau montant
def augmenting_level_path (G, source, sink):
    path = []
    if(nx.has_path(G, source, sink)):
        path = list(nx.shortest_path(G, source, sink))
        print(path)
        return path
    else:
        return False

#----------------------------------------------------------------------------------------------
#Fonction qui vérifie si un chemin est bien à niveau montant
#Input : Un graphe | G 
#Output : Boolean
def check_augmenting_level_path(G, source, sink):
    path = augmenting_level_path(G, source, sink)

    #Si le chemin est disponible, renvoyer True sinon False
    if(path):
        return True
    else:
        return False

#----------------------------------------------------------------------------------------------
#Fonction qui modifie les arcs du à l'algorithme
#Input : Un graphe, un chemin et le minimum de capacité du chemin | G path minCap
#Output : Modfication des arcs
def modify_edges (G, path, minCap):
    #Boucler tant que le chemin est disponible
    for i in range(len(path)-1):
        flow = G.get_edge_data(path[i], path[i+1], "capacity")["capacity"]
        flow = flow - minCap
        nx.set_edge_attributes(G, {(path[i], path[i+1]): {"capacity": flow}})

        #Si la capacité <= 0 on enlève l'arc reliant les deux sommets
        if(G.get_edge_data(path[i], path[i+1], "capacity")["capacity"] <= 0):
            G.remove_edge(path[i], path[i+1])

        #Si un arc entre deux sommets n'est pas disponible, en rajouter un
        if not((path[i+1], path[i]) in G.edges()):
            G.add_edge(str(path[i+1]), str(path[i]), capacity = minCap)
        else:
            flow = G.get_edge_data(path[i+1], path[i], "capacity")["capacity"]
            flow = flow + minCap
            nx.set_edge_attributes(G, {(str(path[i+1]), str(path[i])): {"capacity": flow}})

#----------------------------------------------------------------------------------------------
#Fonction qui calcule le flow maximum d'un réseau de sommets
#Input : Un graphe | G 
#Output : le flow maximum | maxFlow
def dinic_algo (G, source, sink):
    #Vérifier s'il y a un chemin entre la source et le puit pour appliquer l'algorithme
    if(not(has_path(G, source, sink))):
        print()
        print("No path between the source and the sink !")
        return 0

    maxFlow = 0

    #Boucler tant qu'il y a un chemin entre la source et le puit
    while(check_augmenting_level_path(G, source, sink)):

        #Donner le chemin disponible à la variable
        path = augmenting_level_path(G, source, sink)
        #Donner la capacité minimal du chemin
        minCap = min_cap(G, path)
        #Additionner la capacité minimal au flow maximum
        maxFlow = maxFlow + minCap
        #Modifier les arcs à l'aide de l'algorithme de Dinic
        modify_edges(G, path, minCap)

    #Retourner le flow maximum
    return maxFlow
    
#----------------------------------------------------------------------------------------------








    









