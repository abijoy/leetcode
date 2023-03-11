# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        curr = dummy = ListNode()
        while list1 or list2:
            v1 = list1.val if list1 else 101
            v2 = list2.val if list2 else 102
            
            if v1 <= v2:
                temp = v1
                list1 = list1.next
            else:
                temp = v2
                list2 = list2.next
            curr.val = temp 
            if list1 or list2:
                curr.next = ListNode()
                curr = curr.next

        return dummy