# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        seen = set()

        while head:

            if head not in seen:
                seen.add(head)
                head = head.next
            else:
                return True

        return False