
class Graph:
    """
    Un graphe oriente -> G = (X, U)
        - X, un ensemble de sommets
        - U, arcs de G, une famille de X x X
    """

    def __init__(self, som=[], arcs=[]):
        self.X = som
        self.U = arcs

    def printg(self):
        print "X", self.X
        print "U", self.U

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

if __name__ == "__main__":

    som = [1,2,3,4,5]
    arcs = [(1,3), (2,1), (2,3), (2,2), (4,3), (5,3) ,(5,4)]
    g = Graph(som, arcs)
    g.printg()
    print g.pred(3)
    print g.succ(2)
