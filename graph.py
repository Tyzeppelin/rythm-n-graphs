
class Graph:
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
                if (e1, e2) in self.U:
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

if __name__ == "__main__":

    som = [1,2,3,4,5]
    arcs = [(1,3), (2,1), (2,3), (2,2), (4,3), (5,3) ,(5,4)]
    g = Graph(som, arcs)
    g.printg()
    print g.pred(3)
    print g.succ(2)
    g.matrix()
