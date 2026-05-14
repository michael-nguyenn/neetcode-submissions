# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [] # this stores the current head of each linked list
        dummy = ListNode() # deals with empty lists edge cases
        idx = 0 # this is used as a tiebreaker for nodes with the same value

        # go through all lists and add non empty heads to the heap
        for linked_list in lists:
            if linked_list:
                heapq.heappush(heap, (linked_list.val, idx, linked_list))
                idx += 1

        head = dummy
        # now we'll continuously pop and refill the heap
        while heap:

            # Get smallest node and add to the new list
            _, _, smallest_node = heapq.heappop(heap) 
            head.next = smallest_node
            head = head.next

            # Refill heap if possible
            next_node = smallest_node.next
            if next_node:
                heapq.heappush(heap, (next_node.val, idx, next_node))
                idx += 1

        return dummy.next





