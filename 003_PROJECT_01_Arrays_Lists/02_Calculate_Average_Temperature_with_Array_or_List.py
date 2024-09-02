# Calculate Average Temperature with Array/List

# ---------------------------------------------
# finding days above average temperature
# ---------------------------------------------
# This remains same
numDays= int(input("How many days temp? : "))
total = 0

# adding a list Temp to save temperature of days
temp=[]

for i in range(numDays):
    nextDay = int(input("Day " + str(i) + "'s high temp : "))
    # Now, by appending it, the first day will be inserted at the index of zero 
    # and the second day will be inserted at the index of one.
    temp.append(nextDay)
    # Then the total will be calculated based on this list
    total += temp[i]

avg = round(total/numDays,2)
print("Average = " + str(avg))

above = 0
for i in temp:
    if i > avg:
        above += 1

print(str(above) + " days above average")

def missing_number(arr, n):
    total = (n*(n+1))//2
    sum_arr = sum(arr)
    return total-sum_arr