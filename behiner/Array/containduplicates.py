num = [1,2,3,4,5,6,7,9,9,10]
def contain_duplicates(a):
        for i in range(1,len(a)):
            if a[i] == a[i-1]:
                return True
        return False

print(contain_duplicates(num))

"""
have i seen this number before? if yes return true else add it to the set and return false
"""
""" return len(a) != len(set(a))"""