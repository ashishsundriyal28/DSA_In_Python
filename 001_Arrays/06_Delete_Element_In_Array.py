# Creating array with *array* module
from array import *

# created empty array
my_array = array('i', [1,2,3,4,5,6])
print(my_array) # output = array('i', [1, 2, 3, 4, 5, 6])

my_array.remove(2)
print(my_array) # output = array('i', [1, 3, 4, 5, 6])
