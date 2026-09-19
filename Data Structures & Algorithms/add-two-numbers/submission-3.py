# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        
        carry = 0
        cur = head

        while l1 and l2:
            new_val = l1.val + l2.val + carry
            cur.next = ListNode(new_val % 10)
            carry = new_val // 10

            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        # Three scenarios here
        # 1. L1 is longer
        # 2. L2 is longer
        # 3. There is a leftover carry

        while l1:
            new_val = l1.val + carry
            cur.next = ListNode(new_val % 10)
            carry = new_val // 10
            l1 = l1.next
            cur = cur.next
        
        while l2:
            new_val = l2.val + carry
            cur.next = ListNode(new_val % 10)
            carry = new_val // 10
            l2 = l2.next
            cur = cur.next

        if carry > 0:
            cur.next = ListNode(1)

        return head.next

        
        