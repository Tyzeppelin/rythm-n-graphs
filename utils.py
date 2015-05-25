
from graph import *

class StdException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self, value)

class SetUnionException(StdException):
    def __init__(self, value):
        super(SetUnionException, self).__init__(value)

class SetUnknownValueException(StdException):
    def __init__(self, value):
        super(SetUnknownValueException, self).__init__(value)

class UnknownEdgeException(StdException):
    def __init__(self, value):
        super(UnknownEdgeException, self).__init__(value)

class CycleBellmanException(StdException):
    def __init__(self, value):
        super(CycleBellmanException, self).__init__(value)

## Usuals operations on set of edges

#Union of 2 sets
def union(x1, x2):
    return list(set(x1+x2))

# intersection of 2 sets
def intersect(x1, x2):
    inter = []
    for a in x1:
        for b in x2:
            if a == b:
                inter.append(a)
    return inter

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

# True if they are completely different
def isDifferent(x1, x2):
    for e in x2:
        if e in x1:
            return False
    return True

## Others

# True if a is contains in an array containing arrays
def containsDepth2(arr, a):
    for e in arr:
        if a in e:
            return True
    return False

# locate in which cfc a vertex is (I know it's not the correct word, I liek it though)
def locateCfc(cfc, x):
    i = 1
    for a in cfc:
        if x in a:
            return i
        else:
            i += 1
    raise SetUnknownValueException("I can't locate ", x, " in ", cfc)

