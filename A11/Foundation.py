
import random
print("Dice Roller")
print("1.Roll a 6-sided die")
print("2.Roll a 20-sided die")
print("3.Roll multiple dice")
print("4.Exit")
while True:
    ch=int(input("Choose option:"))
    if ch==1:
        roll=random.randint(1,6)
        print("🎲You rolled:",roll)
    elif ch==2:
        roll=random.randint(1,20)
        print("🎲You rolled:",roll)
  
