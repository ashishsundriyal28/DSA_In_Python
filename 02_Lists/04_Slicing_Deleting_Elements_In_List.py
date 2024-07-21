# ----------- SLICING --------------
myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList[0:2]) # output = ['a', 'b']1
# will print only [0: n-1]

print(myList[1:]) # output = ['b', 'c', 'd', 'e', 'f']
# will print only [from 1:till end]

print(myList[:]) # output = ['a', 'b', 'c', 'd', 'e', 'f']
# will print only [from start : till end]

# -- updating using slicing --------
myList[0:2] = ['x', 'y']
print(myList[:]) # output = ['x', 'y', 'c', 'd', 'e', 'f']


# ----------- DELETING --------------
# List methods for deletion
# -> pop()
# -> delete()
# -> remove()

myList = ['a', 'b', 'c', 'd', 'e', 'f']

# a) pop()
# SYNTAX = list_name.pop(index)
# if no index is mentioned, last element will be deleted
myList.pop(1)
print(myList) # output = ['a', 'c', 'd', 'e', 'f']

# b) delete()
# SYNTAX = delete list_name[index]
# multiple elements can be deleted
del myList[1]
del myList[0:2]
print(myList)

# c) remove()
# SYNTAX = list_name.remove('element_name')
myList.remove('e')
print(myList)