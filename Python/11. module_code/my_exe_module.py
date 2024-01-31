# executable module: a module that is also a script


def get_circumference(radius):
    import math
    return 2 * math.pi * radius

# the __name__ of a file will be __main__ if it's executed
# the __name__ of a file will be the file name if it's imported
if __name__ == "__main__": # __main__ is if the file is not imported and this file is run from this page
    radius = input("Enter the radius: ")
    radius = float(radius)
    circumference = get_circumference(radius)
    print(f"The circumference of {radius} is {circumference}")