class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Two Pointers
        # Start it at index one, since first element is always in place
        l = 1

        for r in range(1, len(nums)):
            if (nums[r] != nums[r - 1]):
                nums[l] = nums[r]
                l += 1

        return l