# function: a name for some instructions stored in memory 
# functions are like factories 
# why? I want to be able to reuse this code in lots of places and don't want to duplicate the code again and again
# Functions allow to simplify code and abstract things (abstraction is arguably more important than reuse)
# Abstraction means to break code up into small well-named units
# This file is a module. Retains reusable stuff but does nothing on its own

def say_hello():
    # the instructions in this block may be executed by invoking the function name
    print("Hello")

def say_hello_to(name):
    print("Hello", name)

def print_difference(num1, num2):
    x = num1-num2
    print(str(x))

def get_difference(num1, num2):
    #return is a keyword
    #at most one value may be returned to the caller
    #control of execution passes back to the caller immediately
    return num1-num2


def get_farewell():
    print()
    return "Goodbye"


def get_product(num1, num2):
    return (num1 * num2)

def get_first(cousins):
    return cousins[0]

def get_circumference(radius):
    product = (2 * 3.14 * radius)
    return product


def get_max(list):
    list.remove(min(list))
    list.remove(max(list))
    print(sum(list))