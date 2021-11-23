import random as rdm
import os

#Crée ou utilise un fichier graphe.txt et place des valeurs alétoires de graphe
#Input : /
#Output : Ecriture sur fichier effectué
def generate ():
    try:
        with open("graphe.txt","w") as file:
            file.write("100\n")
            i = 0
            while i<100:
                a = str(rdm.randint(1, 100))
                b = str(rdm.randint(1, 100))
                #Si arc formant boucle -> changer l'arc
                while (a == b):
                    b = str(rdm.randint(1, 100))
                capacity = str(rdm.randint(1, 10))
                #Ecriture des données
                file.write("{} ".format(a))
                file.write("{} ".format(b))
                file.write("{}\n".format(capacity))
                i = i + 1
    except FileNotFoundError:
        print("File was not found !")



