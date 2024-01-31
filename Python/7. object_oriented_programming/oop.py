# object oriented programming: an approach to code that focuses on things (objects)
# object: a group or related variables. These are called attributes in Python (called fields in Java)
#  EVERYTHING in Python IS AN OBJECT
# class: a template for creating objects; every time you create a class, you create a new data type. 
# you're not limited to dictionaries etc, you create your own via a class


# no OO... 
movie = {
    "title" : "Wayne's World",
    "genre" : "Comedy",
    "year"  : 1992, 
    "cast" : ["Mike Meyers", "Dana Carvey"]
}

print(movie["title"])

# WITH OO: Creating a Movie Data type (a class)
class Movie:
    # this is a special dunder method
    # dunder = double underscore
    # dunder method should NEVER be called directly 
    # this method is called when we create Movie objects
    # the first param SHOULD be called self and is a reference to the current object
    def __init__(self, title, genre, year, actors): 
        self.title = title
        self.genre = genre
        self.year = year
        self.actors = actors

    #class data types can have their own functions too 
    def as_csv(self):
        return self.title + "," + self.genre + "," + str(self.year)
    

#---

# This is called instantiation of the Movie Class; Creating an object of type Movie
movie = Movie("Wayne's World","comedy",1992,["Dana Carvey", "Mike Meyers"])
print(movie.title) 
print(movie.as_csv())