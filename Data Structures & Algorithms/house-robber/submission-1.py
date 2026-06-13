class Solution:
    def rob(self, nums: List[int]) -> int:
        value_at_house = {} # this maps house # -> max we can rob there
        
        def dfs(house_num: int) -> int:
            if house_num >= len(nums):
                return 0
            
            if house_num in value_at_house:
                return value_at_house[house_num]
            
            max_value_at_cur_house = max(
                                    nums[house_num] + dfs(house_num + 2), 
                                    dfs(house_num + 1))
            
            value_at_house[house_num] = max_value_at_cur_house
            return max_value_at_cur_house

        return dfs(0)