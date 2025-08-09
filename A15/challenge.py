class ContentCreator:
    def __init__(self,name,followers):
        self.name=name
        self.followers=followers

    def create_content(self):
        pass

class YouTuber(ContentCreator):
    def create_content(self):
        return "Recording and editing videos..."
    
class Blogger(ContentCreator):
    def create_content(self):
        return "Writing and publishing articles..."
    
creators=[YouTuber("Ananya","125K"),Blogger("Vikram","300K")]

for creator in creators:
    print(f"Creator:{creator.name}")
    print(f"Role:{creator.__class__.__name__}")
    print(f"Task:{creator.create_content()}\n")
