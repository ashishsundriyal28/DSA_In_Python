# Creating array with *array* module
from array import *

# created empty array
my_array = array('i', [1,2,3,4,5,6])

def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linearSearch(my_array, 5)) # output = 4
print(linearSearch(my_array, 1)) # output = 0