ls=list()
ans=True
j=40
while True:
    for i in range(1,21):
        if (j%i==0 and (j//i)%2==0):
            ans=True
            ls.append(True)
        else:
            ls.append(False)
            ans=False
            j+=40
            break
    if not ans:
        continue
    else:
        break


if ans:
    #print(ls)
    print('Number that is evenly divisible by numbers 1 to 20 is:',j//2)
else:
    #print(ls)
    print('No number')
             