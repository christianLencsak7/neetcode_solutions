class Solution(object):
    def searchRange(self, nums, target):
        '''
        '''
        leftmost = 0 
        rightmost = len(nums) - 1
        l = 0
        r = len(nums) - 1
        positions = []
        while l <= r: 
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1 
            elif nums[mid] > target:
                r = mid - 1
            else: 
                rightmost = mid
                l = mid + 1
        l = 0
        r = len(nums) - 1
        while l <= r: 
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1 
            elif nums[mid] > target:
                r = mid - 1
            else: 
                leftmost = mid
                r = mid - 1
        if leftmost == 0:
            return [-1, -1]
        else:
            return [leftmost, rightmost]
        