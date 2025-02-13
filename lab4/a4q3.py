def utopiantree(N):
   height=1
   for i in range(1,N+1):
     if i%2==0:
        height=height+1
     else:
        height=height*2
   print(height)
__name__
T=int(input("Enter number of test cases"))
l=[]
for i in range(T):
   N=int(input("Enter the number of growth cycles"))
   l.append(N)
for i in range(T): 
   result=utopiantree(l[i])
