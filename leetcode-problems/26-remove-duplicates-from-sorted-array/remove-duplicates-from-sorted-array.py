class Solution(object):
    def removeDuplicates(self, nums):
        write_index = 1
        for i in range(len(nums)):
            if nums[i] != nums[write_index-1]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index