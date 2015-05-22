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
