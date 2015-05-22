
from graph import *

class SetUnionException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

## Usuals operations on set

#Union of 2 sets
def union(x1, x2):
    return list(set(x1+x2))

# "Composition" of 2 sets (sounds really weird)
def compose(x1, x2):
    comp = []
    for arc1 in x1:
        for arc2 in x2:
            if arc1[1] == arc2[0]:
                comp.append((arc1[0], arc2[1]))
    return comp

# Division of 2 sets
def divide(x1, x2):
    div = x1
    for arc in x2:
        if arc in div:
            div.remove(arc)
    return div

#Make DELTAx (to build a diagonal graph)from a set
def diag(X):
    arcs = []
    for e in X:
        arcs.append((e, e))
    return arcs

# Make complete set of edges to build a complete graph
def complet(X):
    arcs = []
    for x1 in X:
        for x2 in X:
            arcs.append((x1, x2))
    return arcs

# Return True if x2 is a subset of x1
def isSubset(x1, x2):
    big = x1
    for e in x2:
        try:
            big.remove(e)
        except ValueError:
            return False
    return True
