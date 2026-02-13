class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[m] = nums2[m] 
            return nums1
        l, r, r_two = m - 1, m + n - 1, n - 1
        while l >= 0 and r_two >= 0:
            if nums2[r_two] > nums1[l]:
                nums1[r] = nums2[r_two]
                r-= 1
                r_two-= 1
            elif nums2[r_two] < nums1[l]:
                nums1[r] = nums1[l]
                r-= 1
                l-= 1
            else:
                nums1[r] = nums2[r_two]
                r-= 1
                r_two-= 1
        return nums1