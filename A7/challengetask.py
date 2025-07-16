
def sum(a,b):
    return a+b

def diff(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("Simple Calculator")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
ch=int(input("Choose operation:"))
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if ch==1:
    print(f"Result:{sum(a,b)}")
if ch==2:
    print(f"Result:{diff(a,b)}")
if ch==3:
    print(f"Result:{mul(a,b)}")
if ch==4:
    print(f"Result:{div(a,b)}")
