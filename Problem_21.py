def divisorsSum(num):
    s=0
    ls=[]
    for i in range(1,num):
        if num%i==0:
            s+=i
            ls.append(i)P
    return s

AmicablePairSum=0
for j in range(10000):
    sum1=divisorsSum(j)
    sum2=divisorsSum(sum1)
    if j!=sum1 and j==sum2:
        print("Amicable pair is:(",j,",",sum1,")")
        AmicablePairSum+=sum1+sum2
print(AmicablePairSum//2)
