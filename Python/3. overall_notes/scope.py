# scope refers to the visibility and durability of a variable
# globally scoped variable: one that is visible to all functions and lives for the life of the sript
# locally scoped variable: a wall in my livingroom. Visible only within the function in which its declared
# and lives only while the function is executing
#

my_global = "my global variable"

def my_function():
    my_local = "my local variable"
    my_global = 42
    print(my_global)
    print(my_local)

# ---
    
# typically the function call would occur in a separate file (a script)
my_function()

#my_local cannot be accessed outside of my_function
# print(my_local)

print(my_global)

#to write to a global variable in a function ou must prefix the name with global first