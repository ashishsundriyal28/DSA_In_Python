# Accessing/Traversing the List

shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList[0])
# minus index - from the last
print(shoppingList[-1]) # output = Butter
print(shoppingList[-2]) # output = Cheese
# print(shoppingList[-5])  # output = index out of range error

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"++"
    print(shoppingList[i])

# will not print anythng
empty = []
for i in empty:
    print("i am empty")


# *in* operator
# returns True if found, False if not
print('Milk' in shoppingList)
print('Bread' in shoppingList)