'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''

class Solution:
    def pattern13(self,n):
        k=0        
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j+k, end="")
            print()
            k+=i
            
       

k=Solution()
t=int(input("upto "))
#t = 5 #example value
k.pattern13(t)
