p=[0,1,4,7,11,17,17,20,23]
def cut(p,n):
    #initialize list
    r=[0]*(n+1)
    for i in range(1,n+1): #for every length
        q=-12030213 #arbitrary low value
        for j in range(1,i+1): #check up to length
            q=max(q,p[j]+r[i-j]) #optimal is cut at j + optimal of whatever left.
            #check this j times and last value of q is optimal revenue for cut
        r[j]=q

    return r[n]

print [cut(p,i) for i in range(0,len(p))]
