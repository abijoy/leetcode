# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = fast = head
        count = 0
        while fast.next:
            prev = slow
            slow = slow.next
            if not fast.next.next:
                fast = fast.next
            else:
                fast = fast.next.next
            count += 1
        prev.next = slow.next
        return head