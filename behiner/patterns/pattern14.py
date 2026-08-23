'''
A
AB
ABC
ABCD
ABCDE
'''
class Solution:
    def pattern14(self,n):
        k=0        
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j+k, end="")
            print()
            k+=i
            
       

k=Solution()
#t=int(input("upto "))
t = 5 #example value
k.pattern14(t)
