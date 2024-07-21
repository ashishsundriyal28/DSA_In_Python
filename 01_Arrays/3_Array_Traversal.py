# Creating array with *array* module
from array import *

# created empty array
arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.2,3.4,5.6])
print(arr1) # output = array('i', [1, 2, 3, 4, 5, 6])

# arr1.insert(2,9)
# print(arr1)

def traverseArray(array):
    for i in array:
        print(i, end="->")

traverseArray(arr1) # output = 1->2->3->4->5->6->