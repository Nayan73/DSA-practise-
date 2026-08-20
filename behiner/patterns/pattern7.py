class Solution:
    def pattern2(self,n):
        for i in range(1,n+1):
            for k in range(1,n-i+1):
                print(" ", end="")
            for j in range(0,i):
                print("*", end="")
            print()

k=Solution()
#t=int(input("Upto "))
t = 5  # Example value
k.pattern2(t)



"""
for i loop for rows 
for k in range 1 to n+1
    which will print number of empty spaces in according to the row number
for j loop for columns 
    which will print star in according to the row number along with the empty spaces












"""