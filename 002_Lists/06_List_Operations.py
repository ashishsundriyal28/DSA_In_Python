# List Operations

a = [1,2,3]
b = [4,5,6]

# 1. '+' operator => concat
c = a + b
print(c) # output = [1, 2, 3, 4, 5, 6]

# 2. '*' operator => multiply
a = [0]
a = a*4
print(a) # output = [0, 0, 0, 0]


# List Functions


# 1. len() => gives the length of the list
a = [0,1,2,3,4,5,6]
print(len(a)) # output = 7

# 2. max() => gives the max element of the list
a = [0,1,2,3,4,5,6]
print(max(a)) # output = 6

# 3. min() => gives the min element of the list
a = [0,1,2,3,4,5,6]
print(min(a)) # output = 0

# 4. sum() => gives the sum of all element of the list
a = [0,1,2,3,4,5,6]
print(sum(a)) # output = 21
print(sum(a) / len(a)) # average = 3.0


print("--------------------")
myList = list()
while(True):
    inp = input("Enter a number : ")
    if inp == 'done':
        break
    else:
        value = float(inp)
    myList.append(value)

average = sum(myList)/len(myList)

print("Average : ", average)
