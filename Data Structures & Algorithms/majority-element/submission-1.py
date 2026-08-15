class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        res = 0
        cur_max = float('-inf')
        for val in counts:
            if counts[val] > cur_max:
                cur_max = counts[val]
                res = val
        return res
            
        