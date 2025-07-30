Libraries:
random,math,datetime

random:
random.randint(x,y)

datetime:
datetime.date.today
datetime.strptime(bday_input,"%Y-%m-%d").date()==>to make a entered date in the format YYYY-MM-DD to date object
bday.strftime("%A")===> to get the day of the date object


math:
math.pi
math.pow(5,2)
you can import the whole library or just the required funtions from the libraries
from random import choice
colors = ["red","blue"]
print(f"Random color: {choice(colors)
