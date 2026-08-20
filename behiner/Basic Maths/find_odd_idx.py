"""find the even index in an array
a=[2,3,99,2,7]
output 3 """

a=[2,3,99,2,7]
n=int(len(a))
for i in range(n):
    if(a[i]%2==0):
        print(i)
        