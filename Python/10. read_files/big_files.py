# One should NOT USE read() or readlines() for big files
passenger_file = open("passengers.csv")

# by iterating over the file object you can exploit buffering
# you musut do all your processing in the loop
# DO NOT append each line to a list and work with it that way because then you're putting all to memory which is inefficient
# to make it more readable you can abstract into functions
# good news is you can read up to 3 terabytes here
#can make it more performant by increasng the buffer
# if you want to learn how to optimize the reading/writing of very large files, check out iterators/generators
# most files have a method called flush which takes what is in the buffer and then flush it 
for line in passenger_file:
    print(line)

passenger_file.close()