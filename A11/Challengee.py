import random
import string


print("Advanced Password Generator")

while True:
    length=int(input("Password length(8-50):"))
    if 8<=length<=50:
        break
    else:
        print("Enter a number between 8 and 50.")
        

upper=input("Include uppercase letters?(y/n):")
num=input("Include numbers?(y/n):")
sym=input("Include symbols?(y/n):")
exc=input("Exclude similar characters(0,O,I,1)?(y/n):")

characters=string.ascii_lowercase

if upper=='y':
    characters+=string.ascii_uppercase
if num=='y':
    characters+=string.digits
if sym=='y':
    characters+=string.punctuation
if exc=='y':
    for i in "0Oo1Il":
        characters=characters.replace(i,"")

print(characters)
password=""
for i in range(length):
    password+=random.choice(characters)

print(f"Generated password:{password}")

print("Password Analysis:")
if len(password)>=20:
    print(f"Length: Very Strong({len(password)} characters)")
elif len(password)>=12:
    print(f"Length:Strong({len(password)} characters)")
elif len(password)>=8:
    print(f"Length:Weak({len(password)} characters)")

print("Uppercase:Yes" if any(c.isupper() for c in password)else"Uppercase:No")
print("Lowercase:Yes" if any(c.islower() for c in password)else"Lowercase:No")
print("Number:Yes" if any(c.isdigit() for c in password)else"Number:No")
print("Symbols:Yes" if any(c in string.punctuation for c in password)else"Symbols:No")



