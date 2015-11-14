base = 256
#prime to mod stuff with
q=86028121
def rabinKarp(pat,txt):
    M=len(pat)
    N=len(txt)
    p,t,f=0,0,0
    power = 1

    #calculate power
    #needed in sliding window computation
    for i in xrange(M-1):
        power=(power*base)%q

    #calculate the hash of pat, and first window of text
    for i in range(M):
        p=( (base*p)+ord(pat[i]) )%q
        t=( (base*t)+ord(txt[i]) )%q
        if p==t:
            print 'pattern '+pat+' found at position 0'

    # slide the pattern across string
    for i in xrange(M,N):

        #rehash or change sliding window
        t = ( (t-ord(txt[i-M])*power)*base +ord(txt[i])  )%q
        if t==p:
            f=1
            print 'pattern '+pat+' found at position '+str(i-M+1)
    if f==0:
        print 'pattern '+pat+' not in '+txt

#example
rabinKarp('a','aabaax')
