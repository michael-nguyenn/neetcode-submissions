# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        trav = dummy

        while list1 and list2:
            if list1.val < list2.val:
                trav.next = list1
                list1 = list1.next
            else:
                trav.next = list2
                list2 = list2.next

            # Advance trav
            trav = trav.next
        
        # At this point we've completed the shortest list
        # We can connect the remainder of the longer list (if any)
        if list1:
            trav.next = list1
        else:
            trav.next = list2

        return dummy.next


        