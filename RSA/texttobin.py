def transform(textfile, binfile):
    """Transforms a textfile with intgers (only) into
    a binary file"""
    import struct
    f = open(textfile, 'r') #read text mode
    integers = f.read()
    integers = map(int, integers.split())
    f.close()

    N = len(integers)
    b = open(binfile, 'wb') #write binary mode
    count=0
    for value in integers:
        b.write(struct.pack('i', value))
        count+=1
    b.close()
    if count != N:
        print "count: ", count
        print "N: ", N
        print "there was an error"
    return count==N


def readbin(binfile, intsize=4):
    """Reads a binary file with integers and returns them
    into an array"""

    import struct
    binread = open(binfile, 'rb')#binary mode open file
    integers = [] #array to hold integers
    while(True):
        txt = binread.read(intsize) #read next 4 bytes (int size=4)
        if txt == "":
            break #EOF
        #struct.unpack decodes 4 bytes as an int and stores it in a
        #tuple of size 1. using [0] we get the actual number (instead
        #of storing tuples of size 1)
        integers.append(struct.unpack('i', txt)[0])
    binread.close()
    return integers


def main():
    import sys
    if len(sys.argv) != 3:
        print "Use", sys.argv[0]," binfile textfile to transform from textfile to bin"
        sys.exit(1)
    if not transform(sys.argv[2], sys.argv[1]):
        print "there was an error"
        sys.exit(1)
    return 0


if __name__ == "__main__":
    main()
