class Solution(object):
    def isPalindrome(self, x):
        temp=x
        rev=0
        while temp>0:
            reminder=temp%10
            rev=rev*10+reminder
            temp=temp//10
        return x==rev
        