'''
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1
'''

class Solution:
    def pattern11(self, n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                if (i+j)%2!=0:
                    print("0",end=" ")
                else:
                    print("1",end=" ")
                #print(i, end=" ")
            print()

k=Solution()
t=int(input("Upto "))
#t = 5  # Example value'''
k.pattern11(t)
