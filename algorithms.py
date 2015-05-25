
from graph import *
from utils import *

# Trouver la fermeture transitive
def royWarshall(g):
    closure = g.U
    for i in g.X:
        for x in g.X:
            if (x, i) in closure:
                for y in g.X:
                    if (i, y) in closure:
                        if (x, y) not in closure:
                            closure.append((x,y))
    return Graph(g.X, closure)

# Trouver les connexite d'un pont dans un graphe non-oriente
def tarjan(g, a):
    p = []
    d = []
    n = []
    num = []

    #init
    for e in g.X:
        p.append(0)
        d.append(len(g.adja(e)))
        n.append(0)
        num.append(0)
    k = 1
    i = a
    num[a-1] = 1
    p[a-1] = a

    # main step
    while n[i-1] != d[i-1] or i != a:
        if n[i-1] == d[i-1]:
            i = p[i-1] # on remonte dans l'arborescence
        else :
            n[i-1] = n[i-1]+1 # on explore le sommet suivant de gamma(i)
            j = g.adja(i)[n[i-1]-1]
            if p[j-1] == 0:
                 p[j-1] = i
                 i = j
                 k = k+1
                 num[i-1] = k
    return k, num

# Obtenir les cfc de G en utilisant G+
def foulkes(g):
    gpp = royWarshall(g)
    nc = g.X[:] # I slice g.X to get a brand new list. Not a reference
    cfc = []
    for i in g.X:
        if i in nc: # calcul de la cfc de i
            cfci = [i]
            nc.remove(i)
            if (i,i) in gpp:
                for j in g.X[i-1:]:
                    if j in nc:
                        if (i,j) in gpp and (j,i) in gpp:
                            cfci.append(j)
                            nc.remove(j)
            cfc.append(cfci)
    return cfc

# obtenir les ascendants non classes
def ascNonClasse(x, g, nc):
    A = []
    def ancetre(y):
        A.append(y)
        Lpred = intersect(g.pred(y), nc)
        for z in Lpred:
            if z not in A:
                ancetre(z)
    A = []
    ancetre(x)
    return A

# obtenir les descendants non classes
def descNonClasse(x, g, nc):
    D = []
    def fils(y):
        D.append(y)
        Lsuc = intersect(g.succ(y), nc)
        for z in Lsuc:
            if z not in D:
                fils(z)
    D = []
    fils(x)
    return D

# Moore-Dijkstra
def mooreDijkstra(g):
    S = [1]
    L = {1:0}
    pred = dict()

    for i in g.X[1:]:
        if (1, i) in g.U:
            L[i] = g.V[(1,i)]
            pred[i] = 1
        else:
            L[i] = (float("inf"))

    end = False

    while not end:
        sliced = {k:v for k,v in L.items() if k not in S}
        # print sliced, S, g.X
        if min(sliced.values()) == float('inf'):
            end = True
        else:
            i = min(sliced, key=sliced.get)
            S.append(i)
            if set(S) == set(g.X):
                end = True
            else:
                for j in divide(g.succ(i), S):
                    if L[j] > L[i]+g.V[(i,j)]:
                        L[j] = L[i]+g.V[(i,j)]
                    pred[j] = i
    return pred, L
