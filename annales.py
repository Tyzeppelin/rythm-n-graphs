
from graph import *
from operations import *
from algorithms import *
from assertion import *
from utils import *


if __name__ == "__main__":

    print "\t=== 4 Juin 2012 ==="

    print  "1. Stockage des produits"

    print "Q.1 Le nombre minimum de zones de stockage est le cardinal de la clique de cardinal maximal. Il s'agit "\
          "d'un probleme de coloration de graphe. A chaque couleur on associe un lieu de stockage et deux sommets "\
          "adjacents ne peuvent pas avoir la meme couleur."

    print "Q2. On applique la methode du cours/td. C'est a dire on cherche une clique de cardinal maximal (ici {P1,P2,P3})"\
          "et on construit une coloration a partir d'un sommet au hasard. L'algo ici implemente prends les sommets dans"\
          "l'ordre et leur attribut une couleur qui n'est pas l'une d'un de ses voisins"

    X = [1,2,3,4,5,6,7]
    U = [(1,2), (1,3), (1,4), (1,7), (2,3), (3,4), (3,5), (4,5), (4,6), (5,6), (5,7)]
    print "Le graph"
    g = Graph(X, U)
    g.printg()
    nb,col = coloration(g)
    print "Le nombre de couleur ->", nb, ". Une coloration possible ->", col


