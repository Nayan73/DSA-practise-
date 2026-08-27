"""a=[3, 7, 2, 9, 4]

smallest number in array """

a=[3, 7, 2, 9, 4]
s=a[0]
for i in a:
    if i<s:
        s=i
print("Smallest number in array is:", s)