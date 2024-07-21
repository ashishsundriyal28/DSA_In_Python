# Update/Insert in List

# --------- UPDATE -----------------
# myList = [1,2,3,4,5,6,7]
# print(myList)
# myList[2] = 33
# print(myList)

# T.C. = O(1)
# accessing is very efficient and they are just assigning a value over here.

# S.C. = O(1)
# here we don't need an extra memory.
# We have already reserved the memory for a given element.
# We are just changing the value of it.

# --------- INSERT -----------------

# 4 ways of inserting element : 
# Inserting an element to the beginning of the list
# Inserting an element to the any given place in the list
# Inserting an element to the end of the list
# Inserting another list to the list


myList = [1,2,3,4,5,6,7]
print(myList)
# output = [1, 2, 3, 4, 5, 6, 7]

# 1. Inserting an element to the beginning of the list 
# each element has to move one place right, from which element is inserted

# a) .insert function
# SYNTAX = list_name.insert(index_number, value_to_inserted)
myList.insert(0, 11)
print(myList)
# output = [11, 1, 2, 3, 4, 5, 6, 7]
# T.C. = O(N) => everytime element is added, each element is shifted one place right
# S.C. = O(1) => just need one location

# b) .append function => always in the last
# SYNTAX = list_name.append(value_to_inserted)
myList.append(55)
print(myList)
# output = [11, 1, 2, 3, 4, 5, 6, 7, 55]
# T.C. = O(1) => everytime element is added, each element is shifted one place right
# S.C. = O(1) => just need one location

# c) .extend function => can add one list to another list
# SYNTAX = list_name.extend(another_list)
newList = [101,102]
myList.extend(newList)
print(myList)
# output = [11, 1, 2, 3, 4, 5, 6, 7, 55, 101, 102]
# T.C. = O(N) => depend on newList element, but elements are added always one by one
# S.C. = O(N) => depend on newList element