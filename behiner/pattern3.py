"""
1
12
123
1234
"""

class Solution:
    def pattern2(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j, end="")
            print()
       

k=Solution()
t=int(input("upto "))
k.pattern2(t)


