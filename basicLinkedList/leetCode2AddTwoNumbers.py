# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        '''
        16 // 10 = 1 
        16 % 10 = 6 
        '''
        carry = 0
        total = 0
        head= None
        
        if l2 is None:
            return l1 
        elif l1 is None:
            return l2
        while l1 or l2 or carry:
            value1 = 0 
            value2 = 0 
            if l1:
                value1 = l1.val 
            if l2:
                value2 = l2.val
            total = value2 + value1 + carry
            carry = total // 10
            nodevalue= total % 10 
            newval= ListNode(nodevalue)
            if head is None:
                head = newval 
                current = newval
            else:
                current.next = newval
                current = current.next
            if l1 is not None:
                l1=l1.next
            if l2 is not None: 
                l2=l2.next 
        return head 
