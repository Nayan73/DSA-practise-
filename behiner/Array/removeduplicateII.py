"""leetcode 80"""
nums=[1,1,1,2,2,3]
index = 0
for i in range(len(nums)):
    if index < 2 or nums[i] != nums[index-2]:
        nums[index] = nums[i]
        index += 1      


print(nums[:index])