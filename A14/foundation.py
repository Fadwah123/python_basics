class Vehicle:
    def start(self):
        print("Vehicle starting...")
    
class Car(Vehicle):
    def start(self):
        print("Car:Vroom Vroom!")
 
class Bike(Vehicle):
    def start(self):
        print("Bike:Brumm Brumm!")

car=Car()
bike=Bike()
v=Vehicle()
v.start()
car.start()
bike.start()
