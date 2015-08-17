d=[1,4,5,7]

def change(d,x):
    c=[0]*(x+1) # how many coins
    denom=[0]*(x+1)# what coins
    for i in range(1,x+1):
        c[i]=10 #arbitrary large value
        for j in range(0,len(d)): #check every coin
            if i>=d[j] and 1+c[i-d[j]] < c[i]:
                #if it fits the optimal solution is 1 coin plus whatever the optimal is for the i-coin amount
                c[i]=1+c[i-d[j]]
                denom[i]=d[j] #keep coin(s) involved
    return (c,denom)

(c,denom)=change(d,20)
#print c

def printChange(denom,j):
    if j>0:
        print denom[j]
        printChange(denom,j-denom[j])
printChange(denom,13)
