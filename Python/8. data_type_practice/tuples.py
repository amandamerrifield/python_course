my_tuple = tuple()
my_tuple = ()
my_tuple = (1,2,3)
# very similar to lists (but immutable) but ARE NOT meant to be used like lists
# can slice it but can't write to it 


#indexing - you can read from it
first_number = my_tuple[0] # read ok 
# my_tuple[2] = 4 ## ## ## this doesn't work though 

#slicing, iteration and membership is the same


def get_stats(numbers):
    # python automatically wraps returned items in a TUPLE 
    return len(numbers), min(numbers), max(numbers)