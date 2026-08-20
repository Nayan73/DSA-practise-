""" Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

"""
n=int(input("numebr "))
alt=n 
rev=0
while (alt>0):
    reminder=alt%10
    rev=rev*10+reminder
    alt=alt//10

print("reverse ",rev)
print("original ",n)