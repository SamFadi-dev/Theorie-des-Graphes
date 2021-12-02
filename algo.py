import networkx as nx
import matplotlib.pyplot as plt
import random as rdm
from networkx.algorithms.shortest_paths.generic import has_path
import functions as rf

#----------------------------------------------------------------------------------------------
#Fonction qui affiche la liste des sources
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
#Fonction qui affiche la liste des sources
#Input : Un graphe G
#Output : Affichage de la liste | /
def sources_list(G):
    allNodes = list(G.nodes)

    print("List of all source(s) :", end = " ")
    #Boucler toute la liste
    for i in range (len(allNodes)):
        if((not(list(G.predecessors(allNodes[i]))))):
            print(allNodes[i], end= " ")
    print()

#----------------------------------------------------------------------------------------------
#Fonction qui affiche la liste des puits
#Input : Un graphe G
#Output : Affichage de la liste | /
def sinks_list(G):
    allNodes = list(G.nodes)

    print("List of all sink(s) :", end = " ")
    #Boucler toute la liste
    for i in range (len(allNodes)):
        if((not(list(G.successors(allNodes[i]))))):
            print("lol")
            print(allNodes[i], end= " ")
    print()

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
        sources_list(G)
        source = str(input("Give a source : "))

        if not(available_value(G, source)):
            print("Retry : not a node in the graph !")
        elif list(G.predecessors(source)):
            print("Retry : not a source !")
        else:
            check = 1

    check = 0

    #Boucler tant qu'un puit n'est pas trouvé
    while not check:
        print()
        sinks_list(G)
        sink = str(input("Give a sink : "))

        if not(available_value(G, sink)):
            print("Retry : not a node in the graph !")
        elif list(G.predecessors(sink)):
            print("Retry : not a sink !")
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
#Fonction qui retourne le niveau d'un sommet à du chemin le plus court entre la source et la target
#Input : Un graphe, une source et un sommet cible | G source target
#Output : Le niveau du sommet | level
def find_level (G, source, target):
    array = 0
   
    for i in range(1, int(target)+1):
        if(nx.has_path(G, source, str(i))):
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
def all_levels (G, source, sink):
    numberN = nx.number_of_nodes(G)
    allnodes = list(G.nodes)

    #Toujours donner le niveau 0 à la source
    G.nodes[source]["level"] = 0

    #Parcourir tous les sommets du graphe
    for i in range(2, numberN+1):
        #S'il y a un chemin entre la source et le sommet(i), continuer
        if(nx.has_path(G, source, str(i))):
            level = find_level(G, source, str(i))
            #Si le sommet n'a pas de niveau, lui en donner un
            if(("level" in G[str(i)]) == False):
                  G.nodes[str(i)]["level"] = level
        #Sinon lui donner le niveau 0
        else:
            G.nodes[str(i)]["level"] = 0

#----------------------------------------------------------------------------------------------
#Fonction qui retourne le chemin ayant un parcour avec un niveau montant
#Input : Un graphe | G 
#Output : Le chemin avec niveau montant
def augmenting_level_path (G, source, sink):
    paths = []
    if(nx.has_path(G, source, sink)):
        paths = list(nx.shortest_simple_paths(G, source, sink))
    else:
        return paths

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
                    break
                else:
                    count = count + 1
    #Si rien n'a été trouvé, on retourne False
    return paths[i]

#----------------------------------------------------------------------------------------------
#Fonction qui vérifie si un chemin est bien à niveau montant
#Input : Un graphe | G 
#Output : Boolean
def check_augmenting_level_path(G, source, sink):
    path = augmenting_level_path(G, source, sink)

    #Si le chemin es!t disponible, renvoyer True sinon False
    if(path):
        return True
    else:
        return False

#----------------------------------------------------------------------------------------------
#Fonction qui modifie les arcs du à l'algorithme
#Input : Un graphe, un chemin et le minimum de capacité du chemin | G path minCap
#Output : Modfication des arcs
def new_edges (G, path, minCap):
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
def dinic (G, source, sink):
    #Vérifier s'il y a un chemin entre la source et le puit pour appliquer l'algorithme
    if(not(has_path(G, source, sink))):
        print()
        print("No path between the source and the sink !")
        return 0

    maxFlow = 0
    #Initialiser les niveaux des sommets
    all_levels(G, source, sink)

    #Boucler tant qu'il y a un chemin entre la source et le puit
    while(check_augmenting_level_path(G, source, sink)):
        all_levels(G, source, sink)

        #Donner le chemin disponible à la variable
        path = augmenting_level_path(G, source, sink)
        #Donner la capacité minimal du chemin
        minCap = min_cap(G, path)
        #Additionner la capacité minimal au flow maximum
        maxFlow = maxFlow + minCap
        #Modifier les arcs à l'aide de l'algorithme de Dinic
        new_edges(G, path, minCap)

    #Retourner le flow maximum
    return maxFlow
    
#----------------------------------------------------------------------------------------------








    









