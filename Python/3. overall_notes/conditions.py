#conditional statement: a statement composed of 1 or more blocks of which AT MOST ONE will be executed

# # must start with a bool expression
# if 2 > 1:
#     # this block will be executed if the expression is true
#     print("2 is greater than 1")

age = 16
if age >= 18: 
    # This block will be executed if the exp is true
    print("You can vote!")
elif age >= 16:
    print("Almost there")
else:
    print("sorry buddy, no voting for you")
print ("All done!")