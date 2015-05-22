from graph import *
from operations import *
from assertion import *
from algorithms import *
from utils import *



if __name__ == "__main__":

    X = [1,2,3,4,5,6,7]
    U = [(1,2), (1,5), (2,3), (3,4), (4,2), (4,7), (5,4), (5,5), (6,7), (7,6)]

    g = Graph(X, U)
    g.matrix()
    gpp = transitiveClosure(g)
    gpp.matrix()

    print "========\n"

    X1 = [1,2,3,4,5,6]
    U1 = [(1,3), (1,2), (1,4), (1,6), (2,4), (6,4), (4,5)]
    g1 = Graph(X1, U1)
    g1.printg()
    print isConnected(g1)
    print cfcTarjan(g1)
    #a, b =  tarjan(g1, 1)

    print "========\n"

    X2 = [1,2,3,4,5,6]
    U2 = [(1,3), (1,4), (2,3), (3,4), (5,6)]
    g2 = Graph(X2, U2)
    g2.printg()
    print isConnected(g2)
    print cfcTarjan(g2)

    print "========\n"

    X3 = [1,2,3,4,5,6]
    U3 = [(1,2), (2,3), (3,1), (3,4), (3,5), (4,5), (5,4), (6,3)]
    g3 = Graph(X3, U3)
    g3.printg()
    print cfcFoulkes(g3)

    print "========\n"

    print "TD 3 Ex1"
    X4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    U4 = [(1,4), (1,5), (1,6), (2,5), (3,5), (4,3), (5,3), (5,4), (6,7), (7,6), (7,10), (8,6), (8,7), (8,9), (9,6), (9,8), (10,6), (10,11), (11,6), (11,7), (12,1), (12,2), (12,8), (12,13), (12,14), (13,2), (13,9), (13,11), (13,12), (14,2), (14,12)]
    g4 = Graph(X4, U4)
    g.printg()

    print "Q.1 Appliquer Roy-Warshallpour obtenir la fermeture transitive"
    gpp4 = transitiveClosure(g4)
    gpp4.matrix()

    print "Q.2 Donner les cfc par Foulkes"
    print "cfc -> ", cfcFoulkes(g4)

    print "Q.3 donner le graphe reduit"
    g4reduit = reduit(g4)
    g4reduit.printg()

    print "Q.4 Construire un tau-minimal qui soit un graphe partiel de G"
    print "dunno howto yet"
