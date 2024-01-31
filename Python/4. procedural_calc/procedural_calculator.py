# procedural programming is a type of organisation that solves problems using global variable and functions
# total is the calculator's state
# it changes over time as we execute the calc's functions
# many things have state!


total = 0

def add(num):
    # can access global variable by typing global key
    # passing it in the variable like add(sum, total) is redundant    
    global total
    # total = total + num
    # is the same as
    total += num

def subtract(num):
    global total
    total -= num

def multiply(num):
    global total
    total *= num

def divide(num):
    global total
    total /= num

def equals():
    global total
    return_value = total
    total = 0
    return return_value


