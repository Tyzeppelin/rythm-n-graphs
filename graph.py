
from utils import *

class Graph(object):
    """
    Un graphe oriente -> G = (X, U)
        - X, un ensemble de sommets
        - U, arcs de G, une famille de X x X
    """

    def __init__(self, som=[], arcs=[]):
        self.X = som
        self.U = arcs

    def __eq__(self, other):
        return self.X == other.X and self.U == other.U

    def __ne__(self, other):
        return self.X != other.X or self.U != other.U

    def __contains__(self, elt):
        return elt in self.U

    def not__contains__(self, elt):
        return elt not in self.U

    def printg(self):
        print "X", self.X
        print "U", self.U

    # Totally ineffective method
    # But I don't want to be smart
    def matrix(self):
        ss = " |"
        for s in self.X:
            ss+=str(s)+"|"
        for e1 in self.X:
            ss+="\n"+str(e1)+"|"
            for e2 in self.X:
                if (e2, e1) in self.U:
                    ss+="1|"
                else:
                    ss+=" |"
        print ss


    def succ(self, som):
        res = []
        for arc in self.U:
            if arc[0] == som:
                res.append(arc[1])
        return res

    def pred(self, som):
        res = []
        for arc in self.U:
            if arc[1] == som:
                res.append(arc[0])
        return res

    def adja(self, s):
        adj = []
        for arc in self.U:
            if arc[0] == s:
                adj.append(arc[1])
            elif arc[1] == s:
                adj.append(arc[0])
        return adj

    def maxAdja(self):
        adj = 0
        for i in self.X:
            adj = max(adj, len(self.adja(i)))
        return adj


class ValuedGraph(Graph):
    """
    Graphe value
    X -> sommets
    U -> arcs
    V -> value {(x, y): v}
    """

    def __init__(self, som, arc, val):
        super(ValuedGraph, self).__init__(som, arc)
        self.V = val

    def getValue(self, i, j):
        if (i,j) in self.V.keys():
            return self.V[(i,j)]
        elif (j,i) in self.V.keys():
            return self.V[(j,i)]
        else:
            raise UnknownEdgeException("Can't fing the edge ", (i,j), " in ", self.V)

    def printg(self):
        print self.X
        print self.V

if __name__ == "__main__":

    som = [1,2,3,4,5]
    arcs = [(1,3), (2,1), (2,3), (2,2), (4,3), (5,3) ,(5,4)]
    g = Graph(som, arcs)
    g.printg()
    print g.pred(3)
    print g.succ(2)
    g.matrix()
