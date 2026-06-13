class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, sec_prev = 0, 0
        # prev = house right behind cur house
        # sec_prev is two houses behind cur house

        for i in range(len(nums)):
            temp = prev
            prev = max(nums[i] + sec_prev, prev)
            sec_prev = temp

        return prev