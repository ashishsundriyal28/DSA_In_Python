# Creating array with *array* module
import array

# created empty array
my_array = array.array('i') # => T.C. = O(1), S.C.=O(1)
print(my_array) # output = array('i')

my_array1 = array.array('i', [1,2,3,4]) # => T.C. = O(N), S.C.=O(N)
print(my_array1) # output = array('i', [1, 2, 3, 4])

# Syntax => array_name.insert(index, value)
my_array1.insert(200, 6)
print(my_array1) # output = array('i', [1, 2, 6, 3, 4])