def load_contacts():       
    contacts=[]
    with open("contacts.txt", "r") as file:
        for line in file:
            if line.strip():
                name,phone,email=line.strip().split("|")
                contacts.append({"name": name, "phone": phone, "email": email})
    return contacts

def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']}|{contact['phone']}|{contact['email']}\n")

def add_contacts(contacts):
    name=input("Name:")
    phone=input("Phone:")
    email=input("Email:")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact Saved!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\nAll Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact(contacts):
    search_name = input("Enter name to search: ").lower()
    found = False
    for contact in contacts:
        if search_name in contact['name'].lower():
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
    if not found:
        print("Contact not found.")

def delete_contact(contacts):
    delete_name = input("Enter name to delete: ").lower()
    found = False
    for contact in contacts:
        if delete_name in contact['name'].lower():
            contacts.remove(contact)
            found = True
            break  
    if found:
        save_contacts(contacts)
        print("Contact deleted.")
    else:
        print("No matching contact found to delete.")
    return contacts


print("Contact Book")
while True:
    contacts=load_contacts()
    print("1.Add contact")
    print("2.View all contact")
    print("3.Search contact")
    print("4.Delete contact")
    print("5.Exit")
    ch=int(input("Choose option:"))
    if ch==1:
        add_contacts(contacts)
    elif ch==2:
        view_contacts(contacts)
    elif ch==3:
        search_contact(contacts)
    elif ch==4:
        delete_contact(contacts)
    elif ch==5:
        break
    else:
        print("Invalid choice!")
