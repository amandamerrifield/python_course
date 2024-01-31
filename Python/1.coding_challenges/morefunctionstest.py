import functions
#TODO 
# Build and test functions as follows:
# - get_farewell that returns "Goodbye"
# - get_product that returns the product (multiplication) of 2 given numbers
# - get_first that returns the first element of the given list
# - get_circumference that calculates and returns the circle of the given radius
# - - formula 2* PI * r

farewell = functions.get_farewell()

num1 = 14
num2 = 10
product = functions.get_product(num1, num2)

cousins = [
    "Dudley",
    "Matt",
    "Jane",
    "Sarah",
    "Jack",
    "Ted"
]
cousin = functions.get_first(cousins)

radius = 4
circumference = functions.get_circumference(radius)

print(farewell, product, "Hi Cousin", cousin, circumference)

list = [1,5,10,12]
functions.get_max(list)