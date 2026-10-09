class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {} # nums[i] -> idx

        for i in range(len(nums)):
            # We only check the last idx found cause they'll have the smallest abs difference
            if nums[i] in mapping and i - mapping[nums[i]] <= k:
                return True
            
            mapping[nums[i]] = i
        
        return False
        