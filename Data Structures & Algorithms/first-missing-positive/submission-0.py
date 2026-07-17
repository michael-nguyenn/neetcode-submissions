class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # first pass
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # second pass
        for i in range(len(nums)):
            val = abs(nums[i])

            # if value properly slots into the array
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -val
                # else means it's a negative number already
        
        print(nums)

        # third pass we iterate thru the possible answers
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1