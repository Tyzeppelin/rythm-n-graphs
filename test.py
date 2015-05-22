from graph import *
from operations import *
from assertion import *
from utils import *



if __name__ == "__main__":

    X = [1,2,3,4,5,6,7]
    U = [(1,2), (1,5), (2,3), (3,4), (4,2), (4,7), (5,4), (5,5), (6,7), (7,6)]

    g = Graph(X, U)
    g.matrix()
    gpp = transitiveClosure(g)
    gpp.matrix()
