# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        count = 0
        while fast.next:
            slow = slow.next
            if not fast.next.next:
                fast = fast.next
            else:
                fast = fast.next.next
            count += 1
        print(count)
        return slow