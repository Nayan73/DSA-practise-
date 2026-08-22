"""
*****
****
***
**
*
"""


class Solution:
    def pattern5(self,n):
        for i in range(1,n+1):
            for j in range(n,i-1,-1):
                print("*", end="")
            print()
       

k=Solution()
t=int(input("Upto "))
k.pattern5(t)