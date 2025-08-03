Libraries:
random,math,datetime

random:
random.randint(x,y)

datetime:
datetime.date.today
datetime.strptime(bday_input,"%Y-%m-%d").date()==>to make a entered date in the format YYYY-MM-DD to date object
bday.strftime("%A")===> to get the day of the date object
now = datetime.now()
formatted_time = now.strftime("%I:%M %p")
Code	Meaning        	Example
%H	Hour (24-hour)	  14
%I	Hour (12-hour)	  02
%M	Minute	          09
%S	Second	          45
%p	AM/PM	            PM
%A	Weekday	          Tuesday
%d	Day of the month	30
%B	Month name	      July
%Y	Year	            2025


math:
math.pi
math.pow(5,2)
you can import the whole library or just the required funtions from the libraries
from random import choice
colors = ["red","blue"]
print(f"Random color: {choice(colors)
