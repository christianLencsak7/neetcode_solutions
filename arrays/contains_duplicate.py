class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        seen = set()
        for i in range(len(nums)):
            if nums[i - 1] in seen:
                flag = True 
                break
            else:
                seen.add(nums[i - 1])
        return flag 