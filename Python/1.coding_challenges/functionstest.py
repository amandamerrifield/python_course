# to import a module is to copy its code into this script
import functions as functions

# a function call/invocation
# note that it must be prefixed with the module name
functions.say_hello()

#input values are called arguments
functions.say_hello_to("Dave")

my_name = "Amanda"
functions.say_hello_to(my_name)

num1 = 13
num2 = 3

functions.print_difference(num1, num2)

# by setting this to a variable we can use the results for something else
result = functions.get_difference(num1, num2)
