# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pass approach: 
        # We know the index to remove = length - n

        # Get the length
        ll_len = 0
        cur = head
        while cur:
            ll_len += 1
            cur = cur.next

        remove_index = ll_len - n

        # Head edge case
        if remove_index == 0:
            return head.next

        # Now we'll iterate to just before the remove_index
        cur = head
        for i in range(ll_len - 1):
            if (i + 1) == remove_index:
                cur.next = cur.next.next
                break
            cur = cur.next

        return head
