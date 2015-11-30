#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
dictionary = string.digits+string.letters+'?'+'.'+','+' '

def readPrimes(binaryfile='primes.bin', intsize=4):
    """Reads a file of binary encoded primes and returns them
    as an array. Typically the file is primes.bin and each
    int is written as 4 bytes"""
    import struct
    binread = open(binaryfile, 'rb')#binary mode open file
    primes = [] #array to hold primes
    while(True):
        txt = binread.read(intsize) #read next 4 bytes (int size=4)
        if txt == "":
            break #EOF
        #struct.unpack decodes 4 bytes as an int and stores it in a
        #tuple of size 1. using [0] we get the actual number (instead
        #of storing tuples of size 1)
        primes.append(struct.unpack('i', txt)[0])
    return primes


def gcd(a, b):
    """Implements Euclid's algorithm for
    finding the greatest common divisor"""
    if a==0 or b == 0:
        return 0
    if a < 0:
        a = -a
    if b < 0:
        b = -b

    while(True):
        r = a%b
        if not r:
            return b
        a = b
        b = r

def extended_gcd(a, b):
    """Implements Extended Euclid's algorithm
    based on this pseudocode:
    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r / r
        (old_r, r) = (r, old_r - quotient*r)
        (old_s, s) = (s, old_s - quotient*s)
        (old_t, t) = (t, old_t - quotient*t)
    #old_s, old_t are the coefficients. old_r is the gcd
    return (old_s, old_t, old_r)

def coprimes(phi):
    """Return a list of the coprimes of phi"""
    return [e for e in xrange(3, phi+1) if gcd(e, phi)==1]


def generatePrimes():
    """Reads primes from primes.bin and selects two at random"""
    import random
    p, q = random.sample(readPrimes()[10:], 2)
    print "Primes p, q:", p, q
    return (p, q)


def generatePublicKey():
    import random
    """Generates the public key n, e from
    the primes from generatePrimes()"""
    #1. compute two (large) primes p,q, their product n and phi
    p, q = generatePrimes()
    n = p*q
    phi = (p-1)*(q-1)
    print "Parameters n, phi:", n, phi

    #2. select an e such that gcd(e, phi) = 1
    e_candidates = coprimes(phi)
    e = random.choice(e_candidates)

    #3. the public key is e and n.
    #phi is used for the private key (don't return the primes p,q)
    return (e, n, phi)

def generatePrivateKey(phi, e):
    """solves the equation d*e+phi*x = 1 to get the private key d
    using extended_gcd. In case d is negative, transforms it into
    the [1, phi] range
    """

    x, d, gcd = extended_gcd(phi, e)
    if d < 0:
        d = d%phi
    return d


def generateKeyPair():
    """Returns a public/private key pair"""
    e, n, phi = generatePublicKey()
    d = generatePrivateKey(phi, e)
    return (e, n, d)


def encrypt(e, n, message):
    from stringConversion import convert
    num = convert(message)
    return (pow(num, e) % n)

def decrypt(d, n, cryptogram):
    from stringConversion import reverse
    E = pow(cryptogram, d) % n
    return reverse(E)

def main():
    import sys
    from time import time
    if len(sys.argv) < 2:
        print "type help for arguments help"
        sys.exit(1)

    if sys.argv[1] == "help":
        print "TODO: add help here"
        sys.exit(1)

    if sys.argv[1] =="generate":
        print "Generating public/private key pair. Please wait"
        start = time()
        e, n, d = generateKeyPair()
        runtime = time()-start
        print "Keypair generated in", runtime
        print "Public key (e, n):", e, n
        print "Private key (d):", d
        sys.exit(0)

    if sys.argv[1] =="encrypt":
        if len(sys.argv) != 5:
            print "type help for arguments help"
            sys.exit(1)
        e = int(sys.argv[2])
        n = int(sys.argv[3])
        message = sys.argv[4]
        print encrypt(e, n, message)

if __name__=="__main__":
    main()
