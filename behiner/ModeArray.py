"""[4, 2, 7, 2, 9]

Find how many times the number 2 appears."""

a = [4, 2, 7, 2, 9]
count = 0
for i in a:
    if i == 2:
        count += 1
print("The number 2 appears", count, "times.")