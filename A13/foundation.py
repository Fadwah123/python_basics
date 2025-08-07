class Book:
    def __init__(self,title:str,author:str,year:int)->None:
        self.title=title
        self.author=author
        self.year=year

    def summary(self):
        print("Book Summary:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Published: {self.year}")

book1=Book("Atomic Habits","James Clear",2018)
book1.summary()
        
