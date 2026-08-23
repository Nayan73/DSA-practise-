"""
Pattern 7   
    *    
   ***   
  *****  
 ******* 
*********
"""




class Solution:
    def pattern7(self,n):
        for i in range(1,n+1):
            for j in range(n-i):
                print(" ", end="")
            for k in range(2*i-1):
                print("*", end="")
            print()

k=Solution()
t=int(input("Upto "))
'''t = 5  # Example value'''
k.pattern7(t)



"""
for i loop for rows 
for k in range 1 to n+1
    which will print number of empty spaces in according to the row number
for j loop for columns 
    which will print star in according to the row number along with the empty spaces

first for space 
then for stars 
then again spaces 

[4,1,4]
[3,3,3]
[2,5,2]
[1,7,1]
[0,9,0]

"""

'''
using only one loop

for i in range(1,n+1):
    print(""*(n-1) + "*"*(2*i-1))
'''