"""
12345
1234
123
12
1
"""



class Solution:
    def pattern6(self,n):
        for i in range(1,n+1):
            for j in range(1,n+1):
                print(j, end="")
            print()
            n-=1
       

k=Solution()
t=int(input("Upto "))
k.pattern6(t)