class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = { 0 : -1 }
        total = 0

        for i, n in enumerate(nums):
            total += n
            remainder = total % k

            if remainder not in remainders:
                remainders[remainder] = i
            elif i - remainders[remainder] > 1:
                return True
        
        return False

        