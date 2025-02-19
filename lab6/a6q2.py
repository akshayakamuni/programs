def chococakes(K):
    if(K%2==0):
        q=K//2
        r=K-q
    else:
        q=(K+1)//2
        r=K-q
    return r*q
list=[]
T=int(input("Enter the number of test cases"))
for i in range(T):
    K=int(input("Enter the number of times to cut"))
    list.append(K)
for i in range(len(list)):
    result=chococakes(list[i])
    print("maximum number of cakes=",result)