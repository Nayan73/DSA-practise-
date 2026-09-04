class Solution(object):
    def removeDuplicates(self, nums):
        index=0
        for i in range(len(nums)):
            if index <2 or nums[i] != nums[index-2]:
                nums[index] = nums[i]
                index += 1   
        return index 
      
