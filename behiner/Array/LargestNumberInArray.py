a=[3, 7, 2, 9, 4]
l=0
for i in a:
    if i>l:
        l=i

print("Largest number in array is ", l)

"""
by creating a variable l and assigning it to 0,
we can iterate through the array and check if the current element is greater than l 
If it is, we update l to be that element. At the end of the loop, l will hold the largest number in the array.
"""
