a=[ 2, 2, 3, 3,4,4,4,4,5,5]
index = 1
for i in range(len(a)):
    if a[i] != a[index-1]:
        a[index] = a[i]
        index += 1   
print(a[:index])
print (a)

"""
using two pointers, 
first pointer is used to iterate through the array and the second pointer is used to keep track of the unique elements.
If the current element is not equal to the previous unique element, we update the second pointer to
    the current element and increment the second pointer.
    
"""