prev_list = [1,2,3,4]

new_list = []

for i in prev_list:
    multiply_2 = i * 2
    new_list.append(multiply_2)

print(new_list) # output = [2, 4, 6, 8]

# Syntax :
# new_list = [new_item for item in list]

new_list = [i*2 for i in prev_list]
print(new_list) # output = [2, 4, 6, 8]


language = "Python"
new_list = [letter for letter in language]
print(new_list) # output = ['P', 'y', 't', 'h', 'o', 'n']
