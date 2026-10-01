# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        left, right = head, head.next

        while right and right.next:
            if left == right:
                return True

            left = left.next
            right = right.next.next

        return False
        