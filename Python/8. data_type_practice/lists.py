# list: a container that is indexed/ordered and mutable
# - it can grow infinitely (up to memory limit)
# - value, value, value  (no key)
# - duplicates allowed
# - not great for fetching individual values (actually they are very fast at doing so provided you know the index)
# - elements in a list may move around (because it's mutable) so retrieving indexes may be problematic 
# - good for processing every element

# creation 
nums = []
# above is the same meaning as below, just diff ways of writing it - in the below, it is a class 
# it is not the ideal way of instantiating a class, but is good for turning something into a class after the fact
#nums = list()
nums = [1,2,3]

# indexing
first_number = nums[0] #read
nums[2] = 4            #write

# slicing - to obtain a subset of the list into a new variable 
# - first number: starting index (inclusive)
# - second number: ending index (exclusive)
# - third number: step/increment (or decrement); default =  1
letters = ["a", "b", "c", "d", "e", "f", "g"]
slice = letters[2:5] # output: ["c", "d", "e"]
slice = letters[1:6:2] # ["b","d","f"]
slice = letters[::-1] # the list in reverse
print(letters)
print(slice)

#iterating
for letter in letters:
    print(letter)

#membership testing
is_d_in_list = "d" in letters
print(is_d_in_list)

# ALL ABOVE EXERCISES APPLY TO TUPLES AND STRINGS TOO ! :)


# list methods 
artists = ["Rembrandt", "Van Gogh", "Titian"]
artists.append("Van Eyk")
#artists.remove("Rembrandt") #takes out a string literal
artists.pop() # removes a final index item
print(artists)

#built-in functions
nums = [1,2,3,4,5]
print(len(nums)) #gives the length of the list which is 5
print(min(nums))
print(max(nums))
print(sum(nums))
