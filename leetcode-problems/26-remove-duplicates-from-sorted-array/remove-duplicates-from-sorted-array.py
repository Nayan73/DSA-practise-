class Solution(object):
    def removeDuplicates(self, nums):
        writeindex = 1
        for i in range(len(nums)):
            if nums[i] != nums[writeindex-1]:
                nums[writeindex] = nums[i]
                writeindex += 1
        return writeindex