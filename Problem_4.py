import math
def checkPalindrome(n):
    sum,j=0,n
    while n!=0:
        sum=sum*10+n%10
        n//=10
    if sum==j:
        return True
    else: 
        return False

ls=[]
for i in range(100,1000):
    isPalindrome=False
    for j in range(100,1000):
        isPalindrome=checkPalindrome(i*j)
        if isPalindrome:
            ls.append(i*j)
print(ls)
print('Largest palindrome number form multiplying three digits is:',max(ls))
