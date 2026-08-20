"""Check if a number is Armstrong Number or not"""

def IsArmstrong(n):
    alt=n
    count=0
    while alt!=0:
        alt=alt//10
        count += 1

    temp=n
    isarm=0
    while temp>0:
        rem=temp%10
        isarm += rem**count 
        temp=temp//10

    if isarm==n:
        return True
    else:
        return False


n=1634
print(IsArmstrong(n))