import random
num=0
x=random.randint(1,10)
count=1
while(num!=x):
    
    num=int(input("Guess a number(1-10):"))
    if(num<x):
        print("Too low!Try again")
    elif(num>x):
        print("Too high!Try again")
    else:
        print("Correct!You won in",count,"tries")
    count=count+1

