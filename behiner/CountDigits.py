#  number n, return the count of digits in this number.
def CountDigit(n):
    alt=n
    if alt==0:
        return 1 
    count = 0
    while alt!=0:
        alt=alt//10
        count += 1

    return count



n=int(input("number "))
print("number of digits ", CountDigit(n))

    