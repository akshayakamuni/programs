T=int(input("Enter the number of test cases"))
list=[]
for i in range(20):
    list.append(i*i)
for i in range(T):
    count=0
    A=int(input("Enter the starting value"))
    B=int(input("Enter the ending value"))
    for j in range(A,B+1):
        for k in range(len(list)):
              if(j==list[k]):
                count+=1
    print(count)