"""pi=3.14
r=int(input("radius = "))
a=pi*r**2
print(a)
"""
pi=3.14
def area(r):
    global pi
    area = pi*r**2
    return area 


print(area(1))