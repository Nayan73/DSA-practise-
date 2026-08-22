"""
*********
 *******
  *****
   ***
    *
"""

class Solution:
    def pattern8(self,n):
        for i in range(1,n+1):
            #for j in range(n-1,i):
                #print(" ", end="")
            for k in range(2*n-1):
                print("*", end="")
            #for l in range(n-i,i):
             #   print(" ", end="")
            print()

k=Solution()
#t=int(input("Upto "))
t = 5  # Example value'''
k.pattern8(t)


'''
[0,9,0]
[1,7,1]
[2,5,2]
[3,3,3]
[4,1,4]

'''