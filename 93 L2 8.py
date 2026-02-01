def valid(a,b,c):
    if a+b+c==180 and a>0 and b>0 and c>0:
        print("triangle is valid")
    else:
        print("triangle is not valid")
a=int(input("enter angle 1:"))
b=int(input("enter angle 2:"))        
c=int(input("enter angle 3:"))
valid(a,b,c)

