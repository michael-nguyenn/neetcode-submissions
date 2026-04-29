class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()

        for num in nums:
            if num in unique_nums:
                return True
            
            unique_nums.add(num)
        
        return False
        