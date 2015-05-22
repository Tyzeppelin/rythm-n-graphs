
from graph import *

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
