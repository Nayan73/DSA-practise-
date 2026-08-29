n=int(input("number"))
temp=n
rev=0
while n>0:
    reminder=n%10
    rev=rev*10+reminder
    n=n//10
if temp==rev:
    print("yes it is")
else:
    print("no it is not")

