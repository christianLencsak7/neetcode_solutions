class Solution(object):
    def nextGreatestLetter(self, letters, target):
        '''
        Notice that its sorted, good to use binary search for the solution
        a = 65
        c = 67 
        f = 70
        j = 74 
        '''
        min_letter = 0
        max_letter = len(letters) - 1
        while min_letter <= max_letter:
            mid = (max_letter + min_letter) // 2
            if letters[mid] <= target:
                min_letter = mid + 1
            else:
                max_letter = mid - 1
        if min_letter < len(letters):
            return letters[min_letter]
        else:
            return letters[0]