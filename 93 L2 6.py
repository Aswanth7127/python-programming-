def digit(n):
    n=abs(n)
    count=0
    if n==0:
        count=1
    else:
        while n>0:
            count+=1
            n//=10
    print("number of digits",count)
n=int(input("enter number :"))
digit(n)
