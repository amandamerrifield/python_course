num_dirty_dishes = 5

# while num_dirty_dishes > 0:
#     print("Wash a dish", num_dirty_dishes)
#     num_dirty_dishes -= 1

# ---

# what about iterating over a list
names = ["Lebron", "Kobe", "Shaq", "Iverson", "Jordan"]
# index = 0
# # length of a list is always one more than the last index
# while index < len(names):
#     print(names[index])
#     index+=1

# ---
    
# What about iterating when we don't know how many iterations are needed? 
# while True:
#     day = input("Enter the day of the week (1-7): ")
#     day = int(day)
#     if day >= 1 and day <= 7: 
#         print("This is indeed a day. Thank you")
#         break # terminate the loop early since we have what we needed
#     else:
#         print("nope, not a day")

# --
        
# for loops are commonly used to iterate over containers. They can be used to iterate arbitrarily 
for name in names:
    print(name)