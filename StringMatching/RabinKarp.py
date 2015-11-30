BASE = 10 #hash function base

def RabinKarp(text, key):
    positions = []
    keyhash = 0
    N = len(text)
    M = len(key)
    #compute hash of key
    for c in key:
        keyhash = keyhash*BASE+int(c)

    print keyhash
    #compute initial hash of text
    texthash = 0
    for (i, c) in enumerate(key):
        texthash = texthash*BASE+int(text[i])

    print texthash
    if texthash == keyhash:
        positions.append(0)


    #search for match
    for i in range(1, N-M+1):

        #change texthash to scan next part of text
        texthash -= int(str(texthash)[0])*pow(BASE, M-1)
        texthash = texthash*BASE+int(text[M+i-1])
        if texthash < 0:
            texthash+=2**32
        print texthash
        #check for a match in current position
        if texthash==keyhash:
            positions.append(i)
    return positions


text = "101010101"
key = "10"
print RabinKarp(text, key)
