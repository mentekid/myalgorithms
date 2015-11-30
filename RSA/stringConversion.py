BITS = ('0', '1')
ASCII_BITS = 8

def bitlist2str(bitlist):
    """Returns a string in {0,1} from the bitlist"""
    return ''.join([BITS[bit] for bit in bitlist])

def seq2bits(sequence):
    """Returns a sequence of 1s and 0s from a bit sequence"""
    return [0 if bit=='0' else 1 for bit in sequence]

def padding(bits, length):
    """Pads a bit sequence to a certain length"""
    padlen = length-len(bits)
    assert(padlen >= 0)
    return  [0]*(padlen) + bits


def int2bits(n):
    """Converts n to bit array"""
    #bitarray = []
    #if n==0:
    #    return [0]
    #while n > 0:
    #    bitarray.insert(0, n%2) #prepend to array
    #    n /= 2
    #return bitarray
    return map(int, list(bin(n)[2:]))

def str2bits(string):
    c2b = lambda c : padding(int2bits(ord(c)), ASCII_BITS)

    return [b for byte in map(c2b, string) for b in byte]


def bits2char(bits):
    """Converts 8 bits into an ascii char"""
    assert( len(bits) == ASCII_BITS )
    char = 0
    for bit in bits:
        char = char*2 + bit
    return chr(char)

def list2str(p):
    """Converts a python list to a string"""
    return ''.join(p)

def bits2str(bits):
    return ''.join([bits2char(bits[i:i + ASCII_BITS])
        for i in xrange(0, len(bits), ASCII_BITS)])

def convert(string):
    """Return a number for the given string"""
    return int(bitlist2str(str2bits(string)), 2)

def reverse(number):
    """Given a number, return the string"""
    bitarray = seq2bits(bin(number)[2:]) #bin starts with '0b'
    padlen = len(bitarray) + (8 - (len(bitarray) % 8))
    paddedString = padding(bitarray, padlen)
    return bits2str(paddedString)


if __name__ =="__main__":
    string = "attack at dawn"
    converted = convert(string)
    unconverted = reverse(converted)

    print string
    print converted
    print unconverted

