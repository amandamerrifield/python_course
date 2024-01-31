# expression: a statement that yields a new value, e.g. 1 + 1
# + is the addition arithmetic operator 
# x and 1 are operands - the data to be operated on

x = 1
result = x + 1

# arithmetic operators : + - * /(division) % ** (exponent) // (floor division - just the integer without the remainder)
# modulus is % which is to just give the remainder
# Python tried to use the similar symbols to writing

# print (4 ** 2) #16
# print (17 % 4) # remainder is 1

# print("ha" * 3)

# assignment operators: = += -= *= /=
counter = 1 
counter = counter + 1
# the above is the same as the below. The below is shorthand. 
counter += 1

#relational operators: == (equal to) != (NOT equal to) > >= < <= in (is a member of) is (references same object as)
# always produce a boolean result

#print(4==4)
# will produce True

x=5
#print (x==4) #False

# print([] == []) #True
# print(3 >= 3) #True
# print("hi" < "bye") #hi is greater than bye because it looks at it by index and then compares each letter's numeric value
# print(2 in [1,2,3]) #True because the number 2 is in the list. This is a membership test which is true
# print([] is []) # False because "is" is not an alias for ==. "is" is a test of equality of  reference, not content

# list1 = []
# list2 = []
# print(list1 == list2) #True because checking for content
# print(list1 is list2) #False because it's checking if these two names refer to the same list

# list3 = list4 = []
# print (list3 is list4)

# logical operators: and, or, &  not
# price = 7.99
# color = "black"
# # both operands must be true for the result to be true
# print(price < 10 and color == "black")
# # the result is true if either operand is true 
# print(price < 10 or color == "black")
# # NOT produces the inverse of the boolean
# currently_active = True
# print(not currently_active)

#order of precedence
#1. BODMAS = Brackets, Division, Mulitplication, Addition, Subtraction
#2. relational operators
#3. logical operators
#4. assignment
print (4 + 5 < 10 and 9 % 2 > 1)
print(4+5 <10 and 1>1)
print(9<10 and 1>1)
print(True and 1>1)
print(True and False)
print(False)