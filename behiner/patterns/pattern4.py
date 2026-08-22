"""
1
22
333
4444
"""

class Solution:
    def pattern4(self,n):
        for i in range(1,n+1):
            for j in range(0,i):
                print(i, end="")
            print()
       

k=Solution()
t=int(input("Upto "))
k.pattern4(t)
