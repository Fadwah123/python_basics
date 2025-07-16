def peri(l,b):
    return (l+b)*2

def area(l,b):
    return l*b
print("Rectangle calculator")
len=int(input("Length:"))
wid=int(input("Width:"))
print(f"Perimeter:{peri(len,wid)}")
print(f"Area:{area(len,wid)}")
