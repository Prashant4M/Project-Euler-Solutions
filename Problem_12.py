
i,count,ls=1,0,list()
def countFactors(n):
    global count
    global ls
    count=0
    ls=list()
    for i in range(1,n+1):
        if n%i==0:
            ls.append(i)
            count+=1
    return count


while True:
    num=(i*(i+1))//2
    factors=countFactors(num)
    if factors>=500:
        print(num,'=',ls)
        break
    i+=1