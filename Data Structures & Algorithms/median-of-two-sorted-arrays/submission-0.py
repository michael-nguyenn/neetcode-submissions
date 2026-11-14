"""
Problem
- given two sorted arrays of different sizes, need to return the median of all elements
- median is the middle number
    - for odd length, median is the exact middle number
    - for even length, median is the avg of the two middle numbers

Strategy Brute Force
- If we go thru both and merge them then we get O(n+m), then from there we could just take the middle number(s) for median

Strategy Binary Search
[1,2,3,4,4] len=5, half=2
[1,2,4,4]
[3]
- We want to partition our arrays into left and right halves without actually merging them together.
- The size of our left half is len(nums1+nums2)//2
- To do that we'll binary search on the smaller of the two halves
    - the size of our left partition will then be half - mid way of the smaller half
    - if the bounds of our left halves are smaller than the right half of the opposite array, then we've successfully found the left and right partition
    - if our smaller array left is larger than the right side of the larger array, then our left partition on the smaller array is too large, we should make it smaller (right = mid-1)
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2 

        if len(B) < len(A):
            A, B = B, A

        left, right = 0, len(A)-1
        while True:
            i = (left + right) // 2 # mid idx of A
            j = half - i - 2 # -2 is to account for 0 idx in both arrays

            a_left = A[i] if i >= 0 else float("-infinity")
            a_right = A[i+1] if (i+1) < len(A) else float("infinity")
            b_left = B[j] if j >= 0 else float("-infinity")
            b_right = B[j+1] if (j+1) < len(B) else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                if total % 2 != 0:
                    return min(a_right, b_right)
                else:
                    return (min(a_right, b_right) + max(a_left, b_left)) / 2
            elif a_left > b_right:
                right = i-1
            else:
                left = i+1

