import networkx as nx
import matplotlib.pyplot as plt

#Fonction qui permet de lire un graphe au format .txt et crée un graphe NetworkX corréspondant
#Input : filename (nom du fichier à lire)
#Output : création d'un graphe à l'aide de NetworkX
def read_create (filename):
  try:
    with open(filename) as file:
              G = nx.DiGraph()

              #Lire la première ligne
              #Vérifier si le fichier contient au moins un sommet
              nodes = int(file.readline())
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
                      if (count == 1):
                          n2.append(word)
                      if (count == 2):
                          c.append(word)
                      count = count + 1
                  G.add_edge(n1[x], n2[x], capacity = c[x])
                  x = x + 1

              #Erreur si #sommets nuls ou négatifs
              else:
                print("error : graph without nodes !")
              
              
  except FileNotFoundError:
      print("File was not found !")
  return G

#Crée le graphe sous forme de fenêtre visible
#Input : Un graphe
#Output : Le graphe visible
def windowed_graph (G):
  pos = nx.spring_layout(G)
  nx.draw(G, pos, with_labels=True, font_weight='normal')
  nx.draw_networkx_edge_labels(G, pos)
  plt.show()
