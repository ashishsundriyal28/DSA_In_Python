# -------------------------------------
# Ques 1. Pair/Two Sum

# Problem Statement:
# We need to find distinct pairs of indices in a list nums such that the sum of the numbers at those indices equals the target value.
# The function find_pairs(nums, target) should print the indices of such pairs.
# -------------------------------------
# Write a program to find all pairs of integers whose sum is equal to a given number.
# Pairs need to be distinct (2,2), (3,3) can't be counted as pairs

# Example
# find_pairs([1, 2, 3, 2, 3, 4, 5, 6], 6)
# Output : 
# 0 6 => index 0 value = 1, index 6 value = 5 => sum 1+5=6
# 1 5 => index 1 value = 2, index 4 value = 4 => sum 2+4=6
# 3 5 => index 3 value = 2, index 5 value = 4 => sum 2+4=6


def find_pairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)

find_pairs([1, 2, 3, 2, 3, 4, 5, 6], 6)


'''
# Pair/Two sum solution for leetcode

def two_sum(nums, target):
    seen = {}
        
    for i, num in enumerate(nums):
        complement = target - num
            
        if complement in seen:
            print([seen[complement], i])
            return [seen[complement], i]
            
        seen[num] = i
        print(seen)
     
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")
'''