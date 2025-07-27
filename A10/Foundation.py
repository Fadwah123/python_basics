print("Safe calculator")
while True:
    try:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        if b==0:
            print("Error cant divide by zero!")
        else:
            res=a/b
            print(f"Result:{res}")
            break
    except ValueError:
        print("Error:Please enter valid numbers!")
        
