n=int(input("number of terms to be checked"))
for i in range(n):
    num=int(input("Enter the number you want to check"))
    flage=0
    sum=0
    temp=1
    k=0
    sum=k+temp
    while sum<num:
      k=temp
      temp=sum
      sum=temp+k
    if sum==num:
         print("is fibo")
    else:
         print("not fibo")