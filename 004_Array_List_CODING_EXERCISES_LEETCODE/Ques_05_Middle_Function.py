# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Ques 5. Middle Function
# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

# Example
# myList = [1, 2, 3, 4]
# middle(myList)  # [2,3]
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def middle(lst):
    # TODO => myList = [1, 2, 3, 4]
    length_of_list = len(lst)
    if length_of_list == 0:
        return []
    elif length_of_list%2 == 0:
        return lst[length_of_list//2 -1 : length_of_list//2 +1]
    else:
        return lst[length_of_list//2]
    

myList = [1, 2, 3, 4, 5]
print(middle(myList))