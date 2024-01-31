# exception: something unexpected/an error
# we can try to anticipate the unexpected
# two main categories of errors:
# - those that occur because of developer mistakes; should NOT be subject to exception handling
# - those that are environmental 
# Unit testing should pick up programmer errors 

# nums = [1,2,3]
# print(nums[3]) # this will give an index error, and just fix the code

#  --- 

def example():
    while True:
        num = input("Enter a number between 1 and 10: ")
        try:
            num = int(num)
            print("Well done, that's a number. ")
            break
        # the developer should anticipate that something may go wrong here at runtime such as entering a letter
        # this would bec considered an environmental error 
        # ideal number of lines in a try block is ONE because I want to know what line of code caused the problem that breaks it
        except Exception as e:
        # the code in here woul dbe executed if an error is raised
        # if no error is raised the except block is ignored
            print("Numbers only. Try again.")
    
def square(num):
    if type(num) == int or type(num) == float:
        return num ** 2
    else:
        raise Exception(f"{num} is not a number")





