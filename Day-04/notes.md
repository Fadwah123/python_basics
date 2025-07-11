Lists:
Adding:
1)list.append("apple")==>adds apple to end of list
2)list.insert(1,"banana")==>inserts banana at 1st position

Deleting:
1)list.remove("apple")==>remove a particular thing
2)list.pop()==>removes last item

counting:
list.count("apples")==>number of apple occurences

index:
list.index("apple")==>position of apple

sort==>alphabetical order
reverse==>reverse the list
clear==>empty the list

movies = [["knives out", 10], ["titanic", 9]]
to sort this based on rating:
movies.sort(key=lambda x: x[1])  # Ascending

Syntax	                                              What it does
movies.sort()	                                        Sorts alphabetically by movie name (1st item)
movies.sort(key=lambda x: x[1])	                      Sorts by rating (ascending)
movies.sort(key=lambda x: x[1], reverse=True)	        Sorts by rating (descending)
sorted(movies)	                                      Returns a new sorted list (by name)
sorted(movies, key=lambda x: x[1])	                  Returns new list sorted by rating
