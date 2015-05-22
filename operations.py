
from graph import *
from utils import *

# Chap.4 P.4
def union(g1, g2):
    if not g1 == g2:
        raise SetUnionException("g1.X != g2.X")
    return Graph(g1.X, union(s1, s2))

# Chap.4 P.6
def composition(g1, g2):
    if not g1 == g2:
        raise SetUnionException("g1.X != g2.X")
    return Graph(g1.X, compose(g1.U, g2.U))

# Chap.4 P.9
def puissance(g, p):
    if p == 0:
        return Graph(g.X, diag(g.X))
    elif p == 1:
        return g
    else:
        return composition(puissance(g, p-1), g)

# Chap.4 P.11
def transpose(g):
    trans = []
    for arc in g.U:
        trans.append((arc[1], arc[0]))
    return Graph(g.X, trans)

# Chap.4 P.12
def complem(g):
    x2 = complet(g.X)
    return Graph(g.X, divide(x2, g.U))

# Chap.4 P.12
def complemSansBoucle(g):
    d = diag(g.X)
    c = complet(g.X)
    div = divide(divide(c, d), g.U)
    return Graph(g.X, div)

# Transitive Closure AKA Roy-Warshall Algorithm
def transitiveClosure(g):
    closure = g.U
    for i in g.X:
        for x in g.X:
            if (x, i) in closure:
                for y in g.X:
                    if (i, y) in closure:
                        if (x, y) not in closure:
                            closure.append((x,y))
    return Graph(g.X, closure)

