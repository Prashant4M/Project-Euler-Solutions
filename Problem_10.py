def checkPrime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
num,sum,isPrime=2,0,False
while num<2000000 :
    isPrime=checkPrime(num)
    if isPrime:
        sum+=num
    num+=1
print('Sum of prime number till 20 million is:: {}'.format(sum))

