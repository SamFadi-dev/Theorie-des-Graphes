import networkx as nx
import matplotlib.pyplot as plt
import random as rdm
import time

#----------------------------------------------------------------------------------------------
#Fonction qui permet de lire un graphe au format .txt et crée un graphe NetworkX corréspondant
#Input : filename (nom du fichier à lire)
#Output : création d'un graphe à l'aide de NetworkX
def read_create (filename):
  try:
    with open(filename) as file:
              G = nx.DiGraph()

              #Lire la première ligne
              #Vérifier si le fichier contient au moins un sommet
              nodes = file.readline()
              #Si #noeud non disponible
              if((nodes == "\n") or (' ' in nodes)):
                print("No nodes !\n")
                exit()
              nodes = int(nodes)
              if(nodes > 0):
                i = 1
                while (i<=nodes):
                  G.add_node(str(i))
                  i = i+1

                #Lire les éléments des arcs et les placer dans des listes  
                n1 = []
                n2 = []
                c = []
                x = 0
                for line in file:
                  count = 0
                  for word in line.split():
                      if (count == 0):
                          n1.append(word)
                      elif (count == 1):
                          n2.append(word)
                      elif (count == 2):
                          c.append(word)
                      count = count + 1
                  #Vérifier la composition du graphe    
                  if(count != 3):
                    print()
                    print('Wrong Graph composition !')
                    exit()    
                  G.add_edge(n1[x], n2[x], capacity = int(c[x]))
                  x = x + 1
                  

              #Erreur si #sommets nuls ou négatifs
              else:
                print("error : graph without nodes !")
    return G
              
  except FileNotFoundError:
      print("File was not found !")
#----------------------------------------------------------------------------------------------
#Crée le graphe sous forme de fenêtre visible
#Input : Un graphe | G
#Output : Le graphe visible | /
def windowed_graph (G):
  pos = nx.spring_layout(G)
  nx.draw(G, pos, with_labels=True, font_weight='normal')
  nx.draw_networkx_edge_labels(G, pos)
  plt.show()

#----------------------------------------------------------------------------------------------
#Crée ou utilise un fichier graphe.txt et place des valeurs alétoires de graphe
#Input : un naturel | x
#Output : Ecriture sur fichier effectué
def generate (x):
  #Vérifier si le nombre de sommet est valide (> 1)
  if (x > 1):
    try:
        with open("graphe100.txt","w") as file:
            file.write(str(x)+"\n")
            i = 0
            while i<x:
                a = i+1
                b = str(rdm.randint(1, x))
                #Si arc formant boucle -> changer l'arc
                while (a == b):
                    b = str(rdm.randint(1, x))
                capacity = str(rdm.randint(1, 10))
                #Ecriture des données
                file.write("{} ".format(a))
                file.write("{} ".format(b))
                file.write("{}\n".format(capacity))
                i = i + 1
    except FileNotFoundError:
        print("File was not found !")
  else:
    return -1

#----------------------------------------------------------------------------------------------
#Print les informations liées au code
#Input : /
#Output : /
def about():
  print("\n")
  print("University of Liege (2021-2022) \n")
  print("This program is created by 2 computer science students. \n")
  print("SALEHIKATOZI Pouria & EL MASRI Sam \n")
  print("Dinic's algorithm or Dinitz's algorithm is a strongly polynomial algorithm for computing the maximum flow in a flow network, conceived in 1970 by the computer scientist Yefim (Chaim) A. Dinitz.\n")
  print("For more information about Dinic (Dinitz) algorithms: \n")
  print("https://en.wikipedia.org/wiki/Dinic%27s_algorithm \n")
  print("ⒸAll copyrights of this program are reserved for these 2 students. \n")
  time.sleep(3)
#----------------------------------------------------------------------------------------------
