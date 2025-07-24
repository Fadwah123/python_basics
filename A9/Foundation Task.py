print("Daily Diary")
text=input("Enter your thoughts:")
with open("diary.txt","w") as file:
    file.write(text)
print("Your thoughts have been saved to diary.txt")
