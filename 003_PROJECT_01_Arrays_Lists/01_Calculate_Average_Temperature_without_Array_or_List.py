# Calculate Average Temperature without Array/List

numDays= int(input("How many days temp? : "))

total = 0

for i in range(1,numDays+1):
    nextDay = int(input("Day " + str(i) + "'s high temp : "))
    total += nextDay

avg = round(total/numDays,2)
print("Average = " + str(avg))