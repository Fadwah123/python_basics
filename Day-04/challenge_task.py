
print("Shopping List Manager")
shop=[]
while True:
    print("1.Add Item")
    print("2.Remove Item")
    print("3.Show list")
    print("4. Check Item")
    print("5. Exit")
    
    choice=int(input("Enter your choice:"))
    if choice==1:
        item=input("Enter item:")
        shop.append(item)
        print("Added '",item,"'to the list!")
    elif choice==2:
        item=input("Enter the item to remove:")
        shop.remove(item)
        print(item,"removed from the list!")
    elif choice==3:
        print("Your shopping list is:")
        j=1
        for i in shop:
            print(j,".",i)
            j+=1
    elif choice==4:
        item=input("Enter item to check:")
        for i in shop:
            if item==i:
                print("Item in list already!")
                break
            else:
                print("Item not in list!")
    elif choice==5:
        print("Thank you!")
        break
    else:
        print("Invalid choice!Enter choice again!")
