def solve(s):
    n=len(s)
    count=0
    for i in range(n//2):
        count+=abs(ord(s[i])-ord(s[n-i-1]))
    return count
T=int(input("Enter the numbeer of test cases"))
for i in range(T):
    words=input("Enter the string")
    result=solve(words)
    print("for",words,":",result)