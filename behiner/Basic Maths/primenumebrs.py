n=int(input("number "))


"""for i in range (2,n):
    if 
if(n==2 or n==3 or n==5 or n==7):
    print("true it is")
elif(n%2==0):
    print("false")
elif(n%3==0 or n%5==0 or n%7==0):
    print("nhi hai ")
else:
    print("true, it is")
"""

"""
1 and 0 mandatory prime 
2 se upr ka number 
taking k as variable taki answers repeat na ho 
loop me ghuusa 
upto n ko check karna parega 
if none 
    k=false
else 
    true 

"""
"""k="true" 
if n==0 or n==1:
    print("false")
elif n>2:
    for i in range(2,n):
        if (n%i==0):
            k="false"
            break
        

print(k)

"""
#is prime function 

def isPrime(l):
    
    if l==0 or l==1:
        return False
    elif n>2:
        for i in range(2,l):
            if (l%i==0):
                return False
    return True
#this should return bool value(wither true or false)
isPrime(n)

if(isPrime(n)):
    print("this is prime number")
else:
    print("this is not a prime number")