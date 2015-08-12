""" A (slow and lazily written) PageRank implementation you should not use
for anything serious
Author: Yannis Mentekidis
Date: June 2, 2015
"""

from __future__ import division
import numpy
from random import random

"""Returns a variably sparse adjacency matrix given a number of nodes"""
def RandomAdjacencyMatrix(nodes, sparcity=0.65):
    return numpy.matrix([[float((random()>=sparcity)*1) for i in range(nodes)]\
            for i in range(nodes)])

"""Runs PageRank on M for a number of iterations.
beta is the inverse teleportation parameter.
Does not check for convergence"""
def PageRank(M, beta, iterations):
    #initiate v (pagerank vector) and e (teleportation probability)
    v = numpy.matrix([[1.0/len(M)] for i in range(len(M))]) #initial pagerank
    e = v.copy() #not e=v cause that's a pointer.

    #main loop of algorithm
    for i in range(iterations):
        v = beta*M*v + (1-beta)*e
    return v

def MakeStohastic(M):
    for j in range(len(M)):
        colsum = 0
        for i in range(len(M)):
            colsum+= M[i,j]
        if colsum == 0:
            continue
        for k in range(len(M)):
            if M[k,j] == 0:
                continue
            M[k,j] = M[k,j]/colsum
    return M

"""
M = numpy.matrix([[0, 0.5, 0, 0], [1.0/3.0, 0, 0, 1.0/2],\
        [1.0/3.0, 0, 1, 1.0/2], [1.0/3.0, 1.0/2, 0, 0]])
"""
M = RandomAdjacencyMatrix(7, 0.8)
M = MakeStohastic(M)
print M
v = PageRank(M, 0.8, 100)
print v
#TODO: Before running PageRank, convert M to pagerank-compatible (column - stohastic)
