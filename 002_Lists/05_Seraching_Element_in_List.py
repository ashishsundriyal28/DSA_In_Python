my_list = [10,20,30,40,50,60,70,80,90]

# in operator

# T.C. = O(N)
# searches all elements from start to end
# performs Linear Search under the hood

target = 20

if target in my_list:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")


# So enumerate function iterate over the list 
# while also keeping the track of the index of the current item.
# LINEAR SEARCH -> T.C. = O(N), S.C. = O(1)
def linearSerach(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1

print(linearSerach(my_list, 50)) # output => 4