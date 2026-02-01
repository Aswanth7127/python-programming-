def points(cx,cy,r,x,y):
    d2=(x-cx)**2 + (y-cy)**2
    r2=r**2
    if d2<r2:
        print("point inside circle")
    elif d2==r2:
        print("point on the circle")
    else:
        print("point outside circle")
cx=int(input("enter center x :"))
cy=int(input("enter center y :"))
r=int(input("enter radius :"))
x=int(input("enter point x :"))
y=int(input("enter point y :"))
points(cx,cy,r,x,y)
