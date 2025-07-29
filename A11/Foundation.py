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
    elif ch==3:
        num=int(input("How mant dice?"))
        print("You rolled:")
        total=0
        for i in range(0,num):
            x=random.randint(1,6)
            total+=x
            print("🎲",x)
        print("Total:",total)
    elif ch==4:
        break
        
