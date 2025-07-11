print("Top 5 movies")
movie=[]
print("1.Enter 1 to add movies.")
print("2.Enter 2 to display movies based on rating.")
print("3.Enter 3 to display highest and lowest rated movies.")
print("4. Exit")

while True:
    choice=int(input("Enter your choice:"))
    if choice==1:
        if len(movie)>=5:
            print("You can only store 5 movies!")
            
        else:
            name=input("Enter the movie name:")
            rate=int(input("Enter the movie rating(1-10):"))
            movie.append([name,rate])
            print("Movie added!")
            
    elif choice==2:
        if not movie:
            print("Movies list empty.")
        else:
            sorted_movie=sorted(movie,key=lambda x:x[1],reverse=True)
            print(sorted_movie)
    elif choice==3:
            high=max(movie,key=lambda x:x[1])
            low=min(movie,key=lambda x:x[1])
            print("The top rated movie is:",high[0])
            print("The least rated movie is:",low[0])
    elif choice==4:
        print("Exiting!")
        break
    else:
        print("Invalid choice!,please enter a valid choice!")

