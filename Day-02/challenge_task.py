num1=int(input("Enter first number:"))
op=input("Enter the operation(+,-,*,/):")
num2=int(input("Enter second number:"))
if op=="+":
    result=num1+num2
    print("Result:",result)
elif op=="-":
    result=num1-num2
    print("Result:",result)
elif op=="*":
    result=num1*num2
    print("Result:",result)
elif op=="/":
    result=num1/num2
    print("Result:",result)
else:
    print("Invalid choice")
