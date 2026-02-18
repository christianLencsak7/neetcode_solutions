class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_pointer = 0
        right_pointer = len(height) - 1
        max_num = 0 
        temp = 0
        while left_pointer < right_pointer:
            length = right_pointer - left_pointer
            temp = length * min(height[right_pointer], height[left_pointer])
            if temp > max_num:
                max_num = temp
            if height[left_pointer] > height[right_pointer]:
                right_pointer-= 1
            else:
                left_pointer+= 1
        return max_num