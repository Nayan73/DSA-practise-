"""
1      1
12    21
123  321
12344321

"""
class Solution:
    def pattern12(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end="")
            for k in range(2*n-2):
                print(" ",end="")
            for l in range(i,0,-1):
                print(l,end="")
            print()
            n-=1


k=Solution()
#t=int(input("Upto "))
t = 5  # Example value'''
k.pattern12(t)
