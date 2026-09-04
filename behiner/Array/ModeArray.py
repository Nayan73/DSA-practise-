"""find how many times the number 2 appears."""

a = [4, 2, 7, 2, 9]
count = 0
for i in a:
    if i == 2:
        count += 1
print("the number 2 appears", count, "times.")

"""
by creating a variable count and assigning it to 0
 we can iterate through the array and check if the current element is equal to 2
   If it is, we increment count by 1
At the end of the loop, count will hold the number of times 2 appears in the array
"""