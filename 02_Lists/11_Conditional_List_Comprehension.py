# prev_list = [-1, 2, -3, 4, -5, 6]

# # Syntax :
# # new_list = [new_item for item in list if condition]

# new_list = [number**2 for number in prev_list if number>0]
# print(new_list) # output = [2, 4, 6]


# sentence = "My name is Ashish"

# def is_consonant(letter):
#     vowels = "aeiou"
#     return letter.isalpha() and letter.lower() not in vowels

# new_list = [i for i in sentence if is_consonant(i)]
# print(new_list) # output = ['M', 'y', 'n', 'm', 's', 's', 'h', 's', 'h']



prev_list = [-1, 2, -3, 4, -5, 6]

# Syntax :
# new_list = [new_item for item in list if condition]

new_list = [number if number>0 else '-ve number' for number in prev_list]
print(new_list) # output = ['-ve number', 2, '-ve number', 4, '-ve number', 6]

def get_number(number):
    if number>0:
        return number
    else:
        return "-ve no"
    
new_list = [get_number(number) for number in prev_list]
print(new_list) # output = ['-ve no', 2, '-ve no', 4, '-ve no', 6]