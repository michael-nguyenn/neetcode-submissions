class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        num2 = set(nums2)
        res = []

        for num in nums1:
            if num in nums2:
                res.append(num)         

        return res