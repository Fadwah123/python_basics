print("Contact Book")
book={
    "Alice Johnson":
    {"Phone":"555-0123",
     "Email":"alice@email.com",
     "Address":"123 Main St"
    },
    "Bob Smith":
    {"Phone":"555-0456",
     "Email":"bob@email.com",
     "Address":"425 Oak Ave"
    }
}
print("1.Display all contacts.")
print("2.Search by name.")
print("3.Edit contact details.")
print("4.Exit")


while True:
    choice=int(input("Enter choice:"))
    if choice==2:
        search=input("Enter name to search if in the phone book:")
        flag=False

        for i,j in book.items():
            if search.lower()==i.lower():
                for details,value in j.items():
                    print(f"{details}:{value}")
                    flag=True
                    
        if flag==False:
            print("Contact not found!")
    elif choice==1:
        for name in sorted(book):
            print(f"{name}:")
            for feild,value in book[name].items():
                print(f"{feild}:{value}")
        

    elif choice == 3:
        search = input("Enter name to edit: ")
        found = False
        for name in book:
            if search.lower() == name.lower():
                print(f"\nEditing contact: {name}")
                for field in book[name]:
                    current_value = book[name][field]
                    new_value = input(f"{field} [{current_value}]: ")
                    if new_value.strip():
                        book[name][field] = new_value
                print("Contact updated.")
                found = True
                break
        if not found:
            print("Contact not found.")              

    elif choice==4:
        print("Exiting")
        break
    else:
        print("Invalid choice!")
        
        



