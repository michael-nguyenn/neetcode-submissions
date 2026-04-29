class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
                # Two Pointers
        left = 0                # One at the beginning
        right = len(nums) - 1   # One at the end

        # We'll loop until our pointers meet
        while (left <= right):
            # Find the position of our left pointer
            while ((right > 0) and (nums[right] == val)):
                right -= 1

            # Find the position of our right pointer
            while (left < len(nums) and nums[left] != val):
                left += 1
            
            if right <= left: return left

            # Now we can swap
            nums[left] = nums[right]
            nums[right] = val
            right -= 1
            left += 1

        return left