def digital_number(num):
    while num//10!=0: 
       s=0
       while num!=0:
            r=num%10
            s=s+r
            num=num//10
       num=s
    print(num)
num=int(input("Enter the number for which we have to find digital number"))
digital_number(num)