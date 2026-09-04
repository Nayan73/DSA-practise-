"""smallest number in array """

a=[3, 7, 2, 9, 4]
s=a[0]
for i in a:
    if i<s:
        s=i
print("Smallest number in array is ", s)

"""
first we create a variable s and assign it to the first element of the array
then we iterate through the array and check if the current element is less than s
if it is, we update s to be that element
at the end of the loop, s will hold the smallest number in the array
"""