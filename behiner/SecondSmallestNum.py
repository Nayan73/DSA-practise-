"""second smallest number in array without using sort function"""

a = [4, 4, 7, 2]

s = a[0]
s2 = None

for i in a[1:]:
    if s2 is None:
        if i < s:
            s2 = s
            s = i
        elif i > s:
            s2 = i

    elif i < s:
        s2 = s
        s = i

    elif s < i < s2:
        s2 = i

print("Second smallest number is ", s2)