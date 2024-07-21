# List and Strings

# ------------ list conversion of string --------------------
a = "spam"
b = list(a)
print(b)    # output = ['s', 'p', 'a', 'm']

# ------------ split(delimeter) --------------------
a = "spam0-spam1-spam2"
delimeter = "-"
b = a.split(delimeter)
print(b)    # output = ['spam0', 'spam1', 'spam2']


# ------------ join --------------------
a = "spam0-spam1-spam2"
delimeter = "a"
b = a.split(delimeter)
print(b)    # output = ['sp', 'm0-sp', 'm1-sp', 'm2']
print(delimeter.join(b))    # output = spam0-spam1-spam2