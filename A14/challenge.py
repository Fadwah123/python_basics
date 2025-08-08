class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def work(self):
        print("Working...")

class Developer(Employee):
    def work(self):
        print("Writing code...")

class Manager(Employee):
    def work(self):
        print("Managing project...")

employees=[Developer("Ravi",40000),Manager("Priya",60000)]

for i in employees:
    print(f"Employee:{i.name}")
    print(f"Role:{i.__class__.__name__}")
    print(f"Task:",end=" ")
    i.work()
    print()
