class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # once we find the target, we can return immediately
            if nums[mid] == target:
                return mid

            # left side of the array
            if nums[mid] >= nums[left]:
                # target is less than left or greater than mid: Search -->
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                # target is between left and mid: Move right to search <--
                else:
                    right = mid - 1
            # right side of the array
            else:
                # target is > right or less than mid: Move right to search <--
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                # target is between mid and right: Move left to search -->
                else:
                    left = mid + 1

        # making it here means we exited our main loop without finding anything
        return -1