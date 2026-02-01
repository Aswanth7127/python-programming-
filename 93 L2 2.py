def three(a,b,c):
    if a>=b and a>=c:
        largest=a
    elif b>=a and b>=c:
        largest=b
    else:
        largest=c
    if a<=b and a<=c:
        smallest=a
    elif b<=a and b<=c:
        smallest=b
    else:
        smallest=c
    print("largest :",largest)
    print("smallest :",smallest)
a=int(input("enter first number :"))
b=int(input("enter second number :"))
c=int(input("enter third number :"))
three(a,b,c)
