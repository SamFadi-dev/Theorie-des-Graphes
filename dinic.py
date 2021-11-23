import readFile as rf
import networkx as nx
import matplotlib.pyplot as plt
import algo as alg

#Création d'un menu pour l'utilisateur---------------------------------------
ans = True
print("\n")
print("What's your choice ?\n")
while ans:
    print("----------------------------------------------------------------")
    print("1. Apply Dinic's algorithm using a random graph")
    print("2. Apply the Dinic's algorithm using a graph given by the user")
    print("3. exit the program")
    print("----------------------------------------------------------------")
    ans = int(input("\n"))
    #Graphe aléatoire
    if(ans == 1):
        print("\n")
        x = int(input("How much nodes do you need ?\n"))
        rf.generate(x)
        G = rf.read_create("graphe.txt")
        #algo de Dinic ici
        rf.windowed_graph(G)
        print("\n")
    #Graphe fourni par l'utilisateur
    elif(ans == 2):
        print("\n")
        filename = input("What's the name of your .txt file ?\n")
        G = rf.read_create(filename)
        #algo de Dinic ici
        print(alg.count_level(G, 0, "1", "2"))
        rf.windowed_graph(G)
        print("\n")
    #Quitter le programme
    elif(ans == 3):
        print("\n")
        print("Bye bye !\n")
        break
    
    else:
        print("Wrong input, retry!\n")
#-----------------------------------------------------------------------------



          