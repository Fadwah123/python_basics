print("File Reader")
while True:
    try:
        name=input("Enter filename:")
        with open(name,"r") as file:
            content=file.read()
            print(content)
            break
    except FileNotFoundError:
        print(f"Error:File'{name}' not found!")
        ch=input("Would you like to try another file?(y/n):")
        if ch=='n':
            break


