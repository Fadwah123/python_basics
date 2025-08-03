import datetime
import random

mood=["☀️Sunny","🍃Windy","☁️Cloudy","🌧️Rainy","☃️Snowy","⛈️Lightening"]
quotes=[ "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman",
    "Wherever you go, no matter what the weather, always bring your own sunshine. - Anthony J. D’Angelo",
    "Difficult roads often lead to beautiful destinations.",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis"]

print("Daily Inspiration Generator")

now=datetime.datetime.now()
time=now.strftime("%I:%M:%p")
hour=now.hour
if 5 <= hour < 12:
        print (" Good morning!It's",time)
        w_score=9
elif 12 <= hour < 18:
        print ("Good afternoon!It's",time)
        w_score=7
elif 18 <= hour < 22:
        print ("Good evening!It's",time)
        w_score=5
else:
        print ("Good night!It's",time)
        w_score=3
print("\n")

tdy_mood=random.choice(mood)
print("Today's weather mood:",tdy_mood)

if 5<=hour<12:
        print("Time-based energy level: High (Morning boost!)")
        bonus=+2
elif 12<=hour<=18:
        print("Time-based energy level: Medium (Afternoon flow)")
        bonus=+1
elif 18 <= hour < 22:
    print("Time-based energy level: Low (Evening wind-down)")
    bonus=0
else:
    print("Time-based energy level: Very Low (Late night calm)")
    bonus=-1

print("\n")
print("Your inspirational quote:")
tdy_quote=random.choice(quotes)
print(tdy_quote)

print("\n")
print("Mood Calculation:")
print(f"Weather score:{w_score}/10")
print("Time bonus:",bonus)
luck=random.randint(1,10)
print(f"Random luck factor:{luck}/10")
total=w_score*5+bonus*5+luck*5
print(f"Total mood score:{total}/100")

print("1.Get another quote")
print("2.Save this quote to favourites")
print("3.View quote history")
print("4.Exit")
while True:
      ch=int(input("Choose option:"))
      if ch==1:
             new_quote=random.choice(quotes)
             print("Another quote:",new_quote)
      elif ch==2:
               with open("favourites.txt","a")as file:
                      file.write(tdy_quote+"\n")
                      print("Quote added successfully to favourites!")
      elif ch==3:
            print("Quote History")
            try:
                with open("favourites.txt", "r") as file:
                    for i, line in enumerate(file, 1):
                        print(f"{i}. {line.strip()}")
            except FileNotFoundError:
                print("No favorites saved yet.")
      elif ch==4:
            break
      else:
            print("Enter a valid choice!")
