# Creating array with *array* module
from array import *

# created empty array
arr = array('i', [1,2,3,4,5,6])

def accessElement(array, index):
    if index >= len(array):
        print("There is no index in this array")
    else:
        print(f"index {index} in {array} => ", array[index])

accessElement(arr, 0) # output = index 0 in array('i', [1, 2, 3, 4, 5, 6]) =>  1
accessElement(arr, 5) # output = index 5 in array('i', [1, 2, 3, 4, 5, 6]) =>  6
