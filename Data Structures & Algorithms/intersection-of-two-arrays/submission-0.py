"""
Problem
- two arrays, need to return elements that are present in both

Strategy
- if we sort both we'll have them in sorted order. start two pointers
    - if pointers match, then add to res, and advance both
    - if nums1 > nums2, then move nums2 pointer
    - otherwise we move nums1 pointer

Example
     p          p
[4,5,9], [4,4,8,9,9]
- 4 matches, move both 
- 5 > 4, move the 4
- 8 > 5, move the 5
- 9 > 8, move the 8
- 9 matches, move both
- out of bounds, break
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ptr1, ptr2 = 0, 0
        res = set()

        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == nums2[ptr2]:
                res.add(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1
            else: # nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
        
        return list(res)

        