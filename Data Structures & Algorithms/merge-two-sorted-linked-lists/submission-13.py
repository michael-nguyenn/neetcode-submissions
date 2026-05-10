# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases 
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        # we can use a dummy node and then return the node after dummy at the end
        dummy = ListNode()
        cur = dummy

        while (list1 and list2):
            # list1 and list2's pointers will point to the element we're considering adding 
            # to our new_head
            # once we update new_head, list1/list2 will still have reference to the next node
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            
            # no matter the scenario we're always going to advance the cur pointer
            cur = cur.next


        # at this point there will be exactly one list that isn't pointing at None
        if list1:
            cur.next = list1
        else:
            cur.next = list2

        return dummy.next

                