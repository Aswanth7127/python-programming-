def line(x1,y1,x2,y2,x3,y3):
    if (x2-x1)*(y3-y1)==(y2-y1)*(x3-x1):
        print("points lie on the same straight line")
    else:
        print("points do not lie on the same straight line")
x1=int(input("enter x1 :"))       
x2=int(input("enter x2 :"))
x3=int(input("enter x3 :"))
y1=int(input("enter y1 :"))
y2=int(input("enter y2 :"))
y3=int(input("enter y3 :"))
line(x1,y1,x2,y2,x3,y3)
