class Student:
    def __init__(self,name:str,marks:int,roll_number:int):
        self.name=name
        self.marks=marks
        self.roll_number=roll_number

    def display(self):
        print(f"Student: {self.name}")
        print(f"Roll No: {self.roll_number}")
        print(f"Marks: {self.marks}")

    def status(self):
        if self.marks>40:
            print("Status: ✅ Passed")
        else:
            print("Status: ❌ Failed")

s1=Student("Riya Sharma",85,21)
s2=Student("Amil",35,2)
s1.display()
s1.status()
s2.display()
s2.status()
        
