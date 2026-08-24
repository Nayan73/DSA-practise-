class Solution:
    def pattern19(self,n):
        for i in range(n-1,0,-1):
            for j in range(1,i+1):
                print("*",end="")
            for k in range(2*(n-i),0,-1):
                print(" ",end="")
            for l in range(i,0,-1):
                print("*",end="")
            print()
        for i in range(1,n+1):
            for j in range(1,i+1):
                print("*",end="")
            for k in range(2*(n-i),0,-1):
                print(" ",end="")
            for l in range(i,0,-1):
                print("*",end="")
            print()
            

k=Solution()
t=int(input("Upto "))
#t = 5  # Example value'''
k.pattern19(t)
