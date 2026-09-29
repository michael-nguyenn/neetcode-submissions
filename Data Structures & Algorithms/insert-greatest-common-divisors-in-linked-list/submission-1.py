# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        left, right = head, head.next
        while right:
            gcd_node = ListNode(self.find_gcd(left.val, right.val), right)
            left.next = gcd_node
            left = right
            right = right.next

        return head


    def find_gcd(self, a, b):
        gcd = 1
        for i in range(2, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                gcd = i

        return gcd
        