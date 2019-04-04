
def isPrime(n):
    for j in range(2,(n//2)+1):
            if n%j==0:
                return False
    return True
n=600851475143
ls=list()
for i in range(2,n//2):
    prime=False
    if n%i==0:
        prime=isPrime(i)
    if prime:
        ls.append(i)
    else:
        pass
print(ls)
print('Largest prime factor is::',max(ls))
