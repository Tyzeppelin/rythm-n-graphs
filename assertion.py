
from utils import *
from graph import *

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
