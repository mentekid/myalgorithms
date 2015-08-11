#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Computes all possible permutations of [0...N-1] for a given N
If you need the permutations of another array, just use N = len(alist)
and then print alist[perm] for perm in p

Author: Yannis Mentekidis
Date: April 28, 2015
"""

from time import clock
import sys

def all_permutations(N):
    """Recursively find permutations """
    if len(N)==1:
        return [N]
    permutations = []
    for i in range(len(N)):
        p = all_permutations(N[0:i]+N[(i+1):])
        for per in p:
            per.insert(0, N[i])
            permutations.append(per)
    return permutations

def main():
    if len(sys.argv) < 2:
        num = 5 #default
    else:
        if int(sys.argv[1]) > 10:
            print "I don't like pain, so I'm only doing up to 10"
            num = 10
        else:
            num = int(sys.argv[1])

    N = range(num)
    start = clock()
    p = all_permutations(N)
    time = clock() - start
#    print p
    print "Found all ", len(p), " permutations of ", N
    print "Time: %fs" %(time)

if __name__ == "__main__":
    main()
