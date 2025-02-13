word=str(input("Enter a word"))
w=list(word)
C=""
for i in range(len(word)):
    if i%2==1:
         C+=w[i].upper()
    else:
         C+=w[i]
print(C)