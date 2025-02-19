def maxXOR(L,R):
    maxXOR=0
    for i in range(L,R+1):
        for j in range(i,R+1):
            if(maxXOR<i^j):
                maxXOR=i^j
    return maxXOR
L=int(input("Enter th lower limit"))
R=int(input("Enter the upper limit"))
result=maxXOR(L,R)
print("maximal value:",result)