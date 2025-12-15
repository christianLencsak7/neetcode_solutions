class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        output = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashMap:
                difference_index = hashMap[difference]
                if(difference_index > i):
                    output.append(i)
                    output.append(difference_index)
                    return output
                else:
                    output.append(difference_index)
                    output.append(i)
                    return output
            else:
                hashMap[nums[i]] = i