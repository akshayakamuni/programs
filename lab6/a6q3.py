def lexicographybig(ch):
    n=len(ch)
    i=n-2
    while i>=0:
      if(ord(ch[i])==ord(ch[i+1])):
        if(n==2):
           print("no answer")
      i-=1
      if(ord(ch[i])<ord(ch[i+1])):
        temp=ch[i]
        ch[i]=ch[i+1]
        ch[i+1]=temp
        break
      if(ord(ch[i])>ord(ch[i+1])):
        i-=1
    q=''.join(ch)
    print(q)
word=input("enter the string")
word.lower()
ch=[chr for chr in word]
lexicographybig(ch)
