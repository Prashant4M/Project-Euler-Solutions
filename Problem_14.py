i=1
ls=list()
ls1=list()
ls2=list()
while i<100:
    ls=[]
    ls.append(i)
    n=i
    while n!=1:
        if n%2==0:
            ls.append(n//2)
            n=n//2
        else:
            ls.append(3*n+1)
            n=3*n+1
    print(ls)
    ls1.append(len(ls))
    ls2.append(i)
    i+=1
print('Starting number of the sequence:',ls2[ls1.index(max(ls1))],' Length:',max(ls1))

        
