class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        return max(self.helper(nums, 1, len(nums)), self.helper(nums, 0, len(nums) - 1))
    
    def helper(self, nums: List[int], start: int, end: int) -> int:
        rob1, rob2 = 0, 0 # rob1 is two houses ago, rob2 is one house ago

        for i in range(start, end):
            cur_rob = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = cur_rob
        return rob2
        