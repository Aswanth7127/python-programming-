def check(l,b):
    area=l*b
    perimeter=2*(l+b)
    print("area :",area)
    print("perimeter :",perimeter)
    if area>perimeter:
        print("area is greater than perimeter")
    else:
        print("perimeter is greater than area")
l=int(input("enter length :"))
b=int(input("enter breadth :"))
check(l,b)
        
