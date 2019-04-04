numSpellings={1:3,
              2:3,
              3:5,
              4:4,
              5:4,
              6:3,
              7:5,
              8:5,
              9:4}
noOfChars=0
for i in range(1,1000):
    j=i
    while j!=0:
        n=j%10
        if n==1:
            noOfChars+=numSpellings[1]
        if n==2:
            noOfChars+=numSpellings[2]
        if n==3:
            noOfChars+=numSpellings[3]
        if n==4:
            noOfChars+=numSpellings[4]
        if n==5:
            noOfChars+=numSpellings[5]
        if n==6:
            noOfChars+=numSpellings[6]
        if n==7:
            noOfChars+=numSpellings[7]
        if n==8:
            noOfChars+=numSpellings[8]
        if n==9:
            noOfChars+=numSpellings[9]
        j//=10
    if i>100:
        noOfChars+=10

noOfChars+=22
print(noOfChars)
