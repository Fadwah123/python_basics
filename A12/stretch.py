def star(n,count=1):
    if count>n:
        return
    else:
        print("*"*count)
        star(n,count+1)
    
    

n=int(input("Enter how many lines of * needed:"))
print(star(n))
