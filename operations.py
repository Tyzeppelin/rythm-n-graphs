
from graph import *
from algorithms import *
from assertion import *
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
# I won't implement the "calcul des puissances" algorithm. Useless.
def transitiveClosure(g):
    return royWarshall(g)

# Les composantes connexes pour un graphe non-oriente (Tarjan)
def cfcTarjan(g):
    if isConnected(g):
        return [g.X]
    else:
        con = []
        for s in g.X:
            if containsDepth2(con, s):
                continue
            k, num = tarjan(g, s)
            conS = []
            for n in g.X:
                if num[n-1] <= k and num[n-1] != 0:
                    conS.append(n)
            con.append(conS)
        return con

# construit les cfc d'un graphe oriente grace a Foulkes
def cfcFoulkes(g):
    return foulkes(g)

# construit le graphe reduit d'un graphe g
def reduit(g):
    cfc = cfcFoulkes(g)
    n = len(cfc)
    Xc = range(n+1)[1:]
    Uc = []
    i = 1
    for c in cfc:
        Ucc = []
        for x in c:
            for succ in g.succ(x):
                j = locateCfc(cfc, succ)
                Ucc.append((j, i))
        Uc += list(set(Ucc))
        i+=1
    Uc.sort()
    return Graph(Xc, Uc)

# construit les cfc avec l'algo ascendant-descendant
def ascDesc(g):
    nc = g.X[:]
    cfc = []
    for i in g.X:
        if i in nc:
            a = ascNonClasse(i, g, nc)
            d = descNonClasse(i, g, nc)
            cfci = intersect(a, d)
            nc = divide(nc, cfci)
            cfc.append(cfci)
    return cfc

# Les potentiels sont sou la forme (a, b, c)
# tels que a >= b+c
def potentielToV(pot):
    x = []
    u = []
    v = {}
    for (a,b,c) in pot:
        x+=[a,b]
        u.append((b,a))
        v[(b,a)] = c
    return ValuedGraph(list(set(x)), u, v)

def coloration(g):
    k = 2
    colored = False
    coloredNodes = {}
    while not colored:
        coloredNodes = {1:1}
        allColors = range(k+1)[1:]
        for i in g.X[1:]:
            coloredNeigh = [aa for aa in g.adja(i) if aa in coloredNodes.keys()]
            available = divide(allColors, [col for node,col in coloredNodes.items() if node in coloredNeigh])
            if available == []:
                k+=1
                break
            else:
                coloredNodes[i] = available[0]
        if len(coloredNodes) == len(g.X):
            colored = True
    return k, coloredNodes


