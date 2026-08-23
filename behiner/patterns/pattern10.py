'''
*
**
***
****
*****
****
***
**
*
'''

class Solution:
    def pattern10(self, n):
        for i in range(1,n+1):
            for j in range(0,i):
                print("*", end=" ")
            print()
        for i in range(n-1,0,-1):
            for j in range(0,i):
                print("*", end=" ")
            print()


k=Solution()
t=int(input("Upto "))
#t = 5  # Example value'''
k.pattern10(t)
