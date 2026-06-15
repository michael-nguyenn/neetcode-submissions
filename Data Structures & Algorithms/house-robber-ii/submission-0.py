class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0 # rob1 is two houses ago, rob2 is one house ago

        for num in nums:
            cur_rob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = cur_rob
        return rob2
        