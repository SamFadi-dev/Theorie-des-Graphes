import functions as fct
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

    # 1. Graphe aléatoire
    if(ans == 1):
        print("\n")
        x = int(input("How much nodes do you need ?\n"))
        if(fct.generate(x) == -1):
            print("Graph with <= 1 nodes !")
            print("The maximum flow value is 0")
            break
        else:
            G = fct.read_create("graphe100.txt")

        source, sink = alg.source_sink(G)
        maxFlow = alg.dinic_algo(G, source, sink)
        print()
        print("The maximum flow value is "+str(maxFlow))

        fct.windowed_graph(G)
        print("\n")

    # 2. Graphe fourni par l'utilisateur
    elif(ans == 2):
        print("\n")
        filename = input("What's the name of your .txt file ?\n")
        G = fct.read_create(filename)

        source, sink = alg.source_sink(G)
        maxFlow = alg.dinic_algo(G, source, sink)
        print()
        print("The maximum flow value is "+str(maxFlow))

        fct.windowed_graph(G)
        print("\n")

    # 3. Vérification de l'algo avec la fonction dinitz()
    elif(ans == 3):
        print("\n")
        filename = input("What's the name of your .txt file ?\n")
        G = fct.read_create(filename)
        source, sink = alg.source_sink(G)
       
        dinitz(G, source, sink)
        flow_value = nx.maximum_flow_value(G, source, sink)
        print("The maximum flow value is "+str(flow_value))

        fct.windowed_graph(G)
        print("\n")
    # 4. about
    elif(ans == 4):
        fct.about()

    # 5. Quitter le programme
    elif(ans == 5):
        print("\n")
        print("Bye bye !\n")
        break
    
    else:
        print("Wrong input, retry!\n")
#-----------------------------------------------------------------------------



          
