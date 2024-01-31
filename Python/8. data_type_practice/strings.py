# string: an immutable list of characters

# creation
my_str = str() #don't do this unless converting from type x to str

my_str = "Hello"
my_str = 'Hello'

#escape character - used to embed special characters
quote = "Danton said: \"Eat, drink and be merry for tomorrow we die\""
many_lines = "Line 1\nLine2\nLine3"
file_path = "C:\\Users\\Dave\\names.txt" # double \\ means that the \n character doesn't start a new line and stays in the path

# triplequotes
sql = """
select name, email
from clients
where id = 27
"""

# concatenation 
team = {"name" : "Geelong", "premierships": 10}
# don't do the below in 2024 it sucks
# sentence = team["name"] + " has won" + str(team["premierships"]) + " premierships"

# use format string instead
#will format data types and format columns etc 
# may look like this, which specifies the width of the column: f"{team["name"] : 20 }
sentence = f"{team["name"]} has won {team['premierships']} premierships"

#indexing 
greeting = "Hello world"
fifth_character = greeting[4]
#greeting[1] = "u" cannot do this because strings are immutable

#slicing
slice = greeting[6:] #will give "world"

# iterating 
for char in greeting:
    print(char)

# membership testing
print("orl" in greeting) #True

# methods
# there are too many to mention 
# groups: case, alignment, whitespace, search, index of substring, etc

# greeting.upper() this won't work because strings are immutable
# print(greeting)

# greeting_upper = greeting.upper()
# print(greeting_upper)

# OOOOR you can assign it to another variable
# EVERY STRING METHOD MUST RETURN SOMETHING NEW 
greeting = greeting.upper()
print(greeting)