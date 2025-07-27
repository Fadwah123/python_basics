print("Grade Calculator")
while True:
    try:
        n=int(input("How many grades to enter?"))
        sum=0
        for i in range(0,n):
                    grade=int(input(f"Enter grade {i+1}(0-100):"))
                    if grade>100 or grade<0:
                        print("Grade must be between 0 and 100!")
                        break
                    else:
                        sum+=grade
        avg=sum/n
        print(f"Average grade:{avg:.2f}")
        if avg>90:
             print("Letter grade:A")
        elif avg>80:
             print("Letter grade:B")
        elif avg>70:
             print("Letter grade:C")
        elif avg>60:
             print("Letter grade:D")
        elif avg>50:
             print("Letter grade:P")
        elif avg<50:
             print("Letter grade:F")
        break 
    except ValueError:
        print("Error:Please enter a valid number!")
        



