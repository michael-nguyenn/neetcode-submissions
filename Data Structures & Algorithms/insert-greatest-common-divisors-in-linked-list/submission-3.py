# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        left, right = head, head.next
        while right:
            gcd_node = ListNode(math.gcd(left.val, right.val), right)
            left.next = gcd_node
            left = right
            right = right.next

        return head

        