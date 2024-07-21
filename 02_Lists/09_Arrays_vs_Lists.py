# Arrays vs Lists

import numpy as np

# myArray = np.array([1,2,3,4,5,6])
# myList = [1,2,3,4,5]

# print(myArray/2) # output = [0.5 1.  1.5 2.  2.5 3. ]
# print(myList/2) # output = TypeError: unsupported operand type(s) for /: 'list' and 'int'


myArray = np.array([1,2,3,4,5,6,'a'])
myList = [1,2,3,4,5,'a']

print(myArray) # output = ['1' '2' '3' '4' '5' '6' 'a']
print(myList) # output = [1, 2, 3, 4, 5, 'a']