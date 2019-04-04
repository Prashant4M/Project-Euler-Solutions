a,b,sum,c=0,1,0,0
def evenValuedSum():
    global b
    global c
    global a
    global sum
    c=a+b
    if(c%2==0):
        sum+=c
    a=b
    b=c
    print(c)
    return a, b, c, sum

while(c<4000000):
    a, b, c, sum = evenValuedSum()
    
print(sum)


