# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two Pointer Approach
        # If we maintain the distance of n between two pointers
        # Once the right pointer reaches the end, left will be n spots
        # from the end

        # We'll use a dummy node to handle the edge case where we delete the head
        # and start left at dummy, so it lands right before the nth node from the end
        dummy = ListNode(-1, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # At this point the two pointers are n + 1 apart, and we'll advance to the end
        while right:
            left = left.next
            right = right.next

        # Now remove
        left.next = left.next.next

        # We return dummy in the case the original head was removed
        return dummy.next