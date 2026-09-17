class Solution(object):
    def removeElement(self, nums, val):
        index=0
        for i in nums:
            if val!=i:
                nums[index]=i
                index+=1
        return index
        