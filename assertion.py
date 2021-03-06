
from graph import *
from operations import *
from algorithms import *
from utils import *

def isEmpty(g):
    return g.U == []

def isComplete(g):
    return g.U == complet(g.X)

def isDiag(g):
    return g.U == diag(g.X)

# Chap.4 P.4
# True if g1 <= g2
def isBiggerThan(g1, g2):
    if not g1 == g2:
        raise SetUnionException("g1.X != g2.X")
    return isSubset(g1.X, g2.X)

# Chap.5 P.3
def isReflexive(g):
    d = diag(g.X)
    return isSubset(g.X, d)

# Chap.5 P.3
def isAntiReflexive(g):
    d = diag(g.X)
    return isDifferent(d, g.X)

# Chap.5 P.5
def isSymetric(g):
    for arc in g.X:
        if not (arc[1], arc[0]) in g.U:
            return False
    return True

# Chap.5 P.5
def isAntiSymetric(g):
    for arc in g.U:
        if (arc[1], arc[0]) in g.U and arc[0] != arc[1]:
            return False
    return True

# Chap.5 P.7
def isTransitive(g):
    for a1 in g.U:
        for a2 in g.U:
            if a1[1] == a2[0] and (a1[0], a2[1]) not in g.U:
                return False
    return True

# Chap.5 P.8
def isAntiTransitive(g):
    for a1 in g.U:
        for a2 in g.U:
            if a1[1] == a2[0] and (a1[0], a2[1]) in g.U:
                return False
    return True

# I have no idea how to implement the "Fortement anti transitive" thing

# Chap.5 P.30
def tauEqui(g1, g2):
    return transitiveClosure(g1) == transitiveClosure(g2)

# Connexite
def isConnected(g):
    k, num = tarjan(g, g.X[0])
    if k == len(g.X):
        return True
    else:
        return False

# is a stable set
def isStable(g, s):
    for s1 in s:
        for s2 in s:
            if (s1, s2) in g or (s2, s1) in g:
                return False
    return True
