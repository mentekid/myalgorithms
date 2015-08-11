#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Complete program for the compression and decompression of text using Huffman prefix codes
Author: Yannis Mentekidis
e-mail: mentekid@gmail.com
Date: August 11, 2015
"""

import string
import sys
from bisect import bisect

class Node:
    """ An internal node of the Huffman tree"""
    def __init__(self, character, frequency):
        """Initiates a leaf node (character)"""
        self.isLeaf = True
        self.character = character
        self.frequency = frequency
        self.code = -1

    def __repr__(self):
        """Used to print the Huffman Tree"""
        if self.isLeaf:
            return str(self.frequency) + ": " + str(self.character)
        return str(self.frequency)+"\n Left: "+str(self.left)+"\n Right: "+str(self.right)

    def addChildren(self, child1, child2):
        """Adds two children to the Huffman tree"""
        self.isLeaf = False
        self.character = None
        self.frequency = child1.frequency + child2.frequency
        if child1.frequency > child2.frequency:
            #child1 must always be rarer than child2
            (child1, child2) = (child2, child1)
        self.left = child1
        self.right = child2

    def assignCodes(self):
        """Assigns each node a suffix code"""
        if self.isLeaf:
            return
        assert(self.left != None and self.right != None)
        self.left.code = 0
        self.right.code = 1
        self.left.assignCodes()
        self.right.assignCodes()

    def makeDictionary(self, D, code = ''):
        """Extract the dictionary from a code-assigned Huffman tree"""
        if self.code != -1:
            code+=str(self.code)
        if self.isLeaf:
            #leaf nodes are letters
            D[self.character] = code
            return
            #return D #not sure if we should return D or just return
        self.left.makeDictionary(D, code)
        self.right.makeDictionary(D, code)

def countUnique(string):
    """ Counts unique character frequency in string.
    Returns the number of occurences of each character"""
    M = dict()
    for c in string:
        if c in M:
            #increase count for characters that are present
            M[c] +=1
        else:
            #add a new element with count 1 for characters that exist
            M[c] = 1
    return sorted([(x, M[x]) for x in M], key = lambda d :d[1])

def makeHuffmanCodes(string):
    """Creates the huffman codebook from a given string"""
    frequencies = countUnique(string)
    Nodes = [Node(char, freq) for (char, freq) in frequencies]
    assert(len(Nodes) >= 2)
    while len(Nodes) > 2:
        New = Node(None, 0)
        #Merge the two rarest nodes in New
        New.addChildren(Nodes.pop(0), Nodes.pop(0))
        #Insert the new node into the array, keep it sorted
        pos = bisect([X.frequency for X in Nodes], New.frequency)
        Nodes.insert(pos, New) #there might be a more concise way

    #last two nodes in array are the direct descendants of the tree
    Huffman_Tree = Node(None, 0)
    Huffman_Tree.addChildren(Nodes.pop(0), Nodes.pop(0))
    assert (len(Nodes) == 0) #Nodes must be empty now
    #put a code (0/1) in every node except the root
    Huffman_Tree.assignCodes()
    D = dict()
    Huffman_Tree.makeDictionary(D)
    return D

def compress(string, codebook):
    """Given a string and a codebook, compresses the string"""
    return ''.join([codebook[c] for c in string])

def compression():
    """Implements the compression flow"""
    docname = raw_input('Filename to compress: ')
    #open document
    with open(docname) as f:
        text = f.read().splitlines()
    f.close()
    #strip characters other than space, dot, and comma
    include = set(string.ascii_letters + string.digits + ' ' + '.' + ',')
    s = ' '.join(text)
    text = ''.join([ch for ch in s if ch in include])

    #create codebook
    codebook = makeHuffmanCodes(text)

    #compress
    compressed = compress(text, codebook)

    #write the codebook to a file
    codebookname = raw_input('Compression complete. Codebook filename: ')
    with open(codebookname, 'w') as f:
        for key in codebook:
            print >>f, key, ":", codebook[key]
    f.close()

    #write the compressed text to a file
    outputname = raw_input('Output filename: ')
    with open(outputname, 'w') as f:
        print >>f, compressed
    f.close()

def decompression():
    """Implements the decompression flow"""
    codebookname = raw_input('Codebook filename: ')
    inputname = raw_input('Compressed file name: ')

    with open(codebookname) as f:
        codebook = f.read().splitlines()
    f.close()

    #translate codebook to a dictionary. Format expected:
    #c : <binary code>
    d = dict()
    for line in codebook:
        d[line[4:]] = line[0]

    with open(inputname) as f:
        code = f.read() #expects a single-line document
    f.close()

    #decompress code into text using d
    text = ''
    start = 0
    end = 1
    while (end < len(code)):
        while (code[start:end] not in d):
            end +=1 #expand code
        text += d[code[start:end]]
        start = end
        end = end+2

    #decompression complete - write text to file
    outputname = raw_input('Decompression complete. Output file name: ')
    with open(outputname, 'w') as f:
        print >>f, text
    f.close()



def main():
    print "=== Huffman Compression / Decompression ==="
    print "1. Compress text"
    print "2. Decompress text"
    print "3. Exit"
    choice = int(raw_input('Choose: '))
    if choice == 1:
        compression()
    elif choice == 2:
        decompression()
    else:
        sys.exit(0)



if __name__ == "__main__":
    main()
