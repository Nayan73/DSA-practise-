'''
    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *

'''


class Solution:
    def pattern9(self,n):
        """
        for i in range(1,n+1):
            for j in range(n-i):
                print(" ", end="")
            for k in range(2*i-1):
                print("*", end="")
            for l in range(n-i):
                print(" ", end="")
            print()
        for i in range(0,n):
                    for j in range(i):
                        print(" ", end="")
                    for k in range(2*n-1,0,-1):
                        print("*", end="")
                    for l in range(i,):
                        print(" ", end="")
                    print()
                    n-=1
        """
        for i in range (1,n+1):
            print(" "*(n-i)+"*"*(2*i-1))
        for i in range (n,0,-1):
            print(" "*(n-i)+"*"*(2*i-1))

k=Solution()
t=int(input("Upto "))
'''t = 5  # Example value'''
k.pattern9(t)


'''
[4,1,4]
[3,3,3]
[2,5,2]
[1,7,1]
[0,9,0]
[0,9,0]
[1,7,1]
[2,5,2]
[3,3,3]
[4,1,4]
'''