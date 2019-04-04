import array
def checkPrime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

number=2
i=1
ls=list()
while i<=10001 :
    isPrime=checkPrime(number)
    if isPrime:
        ls.append(number)
        i+=1
    number+=1
print(ls)
print('10001th prime number:',ls.pop())

