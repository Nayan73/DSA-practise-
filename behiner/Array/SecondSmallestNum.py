"""second smallest number in array """

a = [4, 4, 7, 2]

s = a[0]
s2 = None

for i in a[1:]:
    if s2 is None:
        if i < s:
            s2 = s
            s = i
        elif i > s:
            s2 = i

    elif i < s:
        s2 = s
        s = i

    elif s < i < s2:
        s2 = i

print("Second smallest number is ", s2)

"""
first we create two variables s and s2, 
s is assigned to the first element of the array and s2 is assigned to None
then we iterate through the array starting from the second element
if s2 is None, we check if the current element is less than s

if it is, we update s2 to be s and s to be the current element
if it is greater than s, we update s2 to be the current element 
if s2 is not None, we check if the current element is less than s
if it is, we update s2 to be s and s to be the current element
if it is greater than s and less than s2, we update s2 to be the current element
At the end of the loop, s2 will hold the second smallest number in the array
"""