# Creating array with *array* module
# see the type code in the above image, 
# eg :- i -> integer type
import array

# created empty array
my_array = array.array('i') # --------- T.C. = O(1), S.C.=O(1)
print(my_array) # output = array('i')

# my_array1 = array.array('i', [1,2,3,4'a'])    # error
my_array1 = array.array('i', [1,2,3,4]) # --------- T.C. = O(N), S.C.=O(N)
print(my_array1) # output = array('i', [1, 2, 3, 4])


import numpy as np

# Created empty array using numpy
np_array = np.array([], dtype=int)  # --------- T.C. = O(1), S.C.=O(1)
print(np_array) # output = []
np_array1 = np.array([1,2,3,4]) # --------- T.C. = O(N), S.C.=O(N)
print(np_array1) # output = [1 2 3 4]