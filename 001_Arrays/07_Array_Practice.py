# Created by Elshad Karimov
# Practiced by Ashish Sundriyal
# Copyright - All rights reserved
from array import *

# 1. Create an array and traverse

my_array = array('i', [1,2,3,4,5])
for i in my_array:
    print(i, end=' ')
print()
# T.C. = O(N)


# 2. Access individual elements through indexes.
print("-------- Step 2 ------------")
print(my_array[0])


# 3. Append any value to the array using append()
print("-------- Step 3 ------------")
my_array.append(6)
for i in my_array:
    print(i, end=' ')
print()
# T.C. = O(1)

# 4. Insert value in an array using insert() method
print("-------- Step 4 ------------")
my_array.insert(3, 11)
for i in my_array:
    print(i, end=" ")
print()

# 5. Extend python array using extend() method
print("-------- Step 5 ------------")

my_array1 = array('i', [10,11,12])
my_array.extend(my_array1)
for i in my_array:
    print(i, end=" ")
print()

# 6. Add items from list into array using fromlist() method
print("-------- Step 6 ------------")

tempList = [20,21,22]
my_array.fromlist(tempList)
for i in my_array:
    print(i, end=" ")
print()

# 7. Remove Any array element using remove() method
print("-------- Step 7 ------------")
# my_array.remove(element)

# remove function works like this when it finds the first occurrence of the value in the array 
# then it removes it and that's it, 
# it does not continue to find another occurrence of this array.
# T.C. = O(N)

my_array.remove(11)
for i in my_array:
    print(i, end=" ")
print()

# 8. Remove last array element using pop() method
print("-------- Step 8 ------------")
# my_array.remove(element)

my_array.pop()
for i in my_array:
    print(i, end=" ")
print()

# 9. Fetch any element through its index using index() method
print("-------- Step 9 ------------")
print(my_array[2])


# 10. Reverse a python array using reverse() method
print("-------- Step 10 ------------")
my_array.reverse()
for i in my_array:
    print(i, end=" ")
print()


# 11. Get array buffer information through buffer_info() method
print("-------- Step 11 ------------")
print(my_array.buffer_info())
print()


# 12. Check for number of occurrences of an element using count() method
print("-------- Step 12 ------------")
print(my_array.count(11))
print()
# 13. Convert array to string using tostring() method
print("-------- Step 13 ------------")
array_bytes = my_array.tobytes()
print(array_bytes)
print()

# 14. Convert array to a python list with same elements using tolist() method
print("-------- Step 14 ------------")
arr_l = my_array.tolist()
print(type(arr_l))
print()

# 15. Append a string to char array using fromstring() method
print("-------- Step 15 ------------")
char_arr = array('u', ['a', 'b', 'c'])
char_arr.append('r')
for i in char_arr:
    print(i, end=" ")
print()

# 16. Slice Elements from an array
print("-------- Step 16 ------------")
sliced_elements = my_array[1:5]

for i in sliced_elements:
    print(i, end=" ")
