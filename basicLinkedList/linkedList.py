# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list2 is None:
            return list1 
        elif list1 is None:
            return list2
        elif list1.val > list2.val:
            list2.next =  self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next =  self.mergeTwoLists( list1.next, list2)
            return list1
        



        ''' 
        if current is None: # Base case: end of the list
            return 
        else:              
            return traverse_linked_list(current.next)
        def traverse_linked_list(head):
            return traerse_linked_list(current.next)
        if not list1 or not list2
            return CommonNodes
        if list1.val < list2.val:
            return mergeTwoLists(self, list1.next, list2)
        elif list1.val > list2.val:
            return mergeTwolists(self, list1, list2.next)
        else:
            CommonNodes.append(list1.val)
            return mergeTwoLists(list1.next, list2.next)
        '''