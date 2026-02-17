class Solution(object):
    def removeDuplicates(self, nums):
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == nums[r]:
                r += 1
            elif nums[r] > nums[l]:
                l += 1 
                nums[l] = nums[r]
        return l + 1