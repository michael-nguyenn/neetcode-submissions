# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        # since fast moves 2 nodes at a time 
        # we need to make sure fast -> to access fast.next
        # fast.next -> to access fast.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False