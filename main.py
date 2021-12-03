import functions as rf
import networkx as nx
import matplotlib.pyplot as plt
import algo as alg
from networkx.algorithms.flow import dinitz

#Création d'un menu pour l'utilisateur---------------------------------------
ans = True
print("\n")
print("What's your choice ?\n")
while ans:
    print("----------------------------------------------------------------")
    print("1. Apply Dinic's algorithm using a random graph")
    print("2. Apply the Dinic's algorithm using a graph given by the user")
    print("3. Check the Dinic's algorithm with NetworkX function")
    print("4. About")   
    print("5. Exit the program")
    print("----------------------------------------------------------------")
    ans = int(input("\n"))

    #Graphe aléatoire
    if(ans == 1):
        print("\n")
        x = int(input("How much nodes do you need ?\n"))
        if(rf.generate(x) == -1):
            print("Graph with <= 1 nodes !")
            print("The maximum flow value is 0")
            break
        else:
            G = rf.read_create("graphe100.txt")

        source, sink = alg.source_sink(G)
        maxFlow = alg.dinic(G, source, sink)
        print()
        print("The maximum flow value is "+str(maxFlow))

        rf.windowed_graph(G)
        print("\n")

    #Graphe fourni par l'utilisateur
    elif(ans == 2):
        print("\n")
        filename = input("What's the name of your .txt file ?\n")
        G = rf.read_create(filename)

        source, sink = alg.source_sink(G)
        maxFlow = alg.dinic(G, source, sink)
        print()
        print("The maximum flow value is "+str(maxFlow))

        rf.windowed_graph(G)
        print("\n")

    #Vérification de l'algo avec la fonction dinitz()
    elif(ans == 3):
        print("\n")
        filename = input("What's the name of your .txt file ?\n")
        G = rf.read_create(filename)
        source, sink = alg.source_sink(G)
       
        dinitz(G, source, sink)
        flow_value = nx.maximum_flow_value(G, source, sink)
        print("The maximum flow1 value is "+str(flow_value))

        rf.windowed_graph(G)
        print("\n")
    #about
    elif(ans == 4):
        print("\n")
        print("University of Liege (2021-2022) \n")
        print("This program is created by 2 computer science students. \n")
        print("SALEHIKATOZI Pouria & EL MASRI Sam \n")
        print("Dinic's algorithm or Dinitz's algorithm is a strongly polynomial algorithm for computing the maximum flow in a flow network, conceived in 1970 by the computer scientist Yefim (Chaim) A. Dinitz.\n")
        print("For more information about Dinic (Dinitz) algorithms: \n")
        print("https://en.wikipedia.org/wiki/Dinic%27s_algorithm \n")
        print("ⒸAll copyrights of this program are reserved for these 2 students. \n")

    #Quitter le programme
    elif(ans == 5):
        print("\n")
        print("Bye bye !\n")
        break
    
    else:
        print("Wrong input, retry!\n")
#-----------------------------------------------------------------------------



          
