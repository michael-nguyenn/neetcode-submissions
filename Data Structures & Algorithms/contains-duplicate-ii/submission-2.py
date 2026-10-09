"""
Problem
- Find two distinct indices such that the two numbers equal the same and 
- Their absolute difference is <= k

Example
 0 1 2 3
[1 2 3 1]

 0 1 2
[2 1 2]

Strategy
- Brute force would be checking every combo O(n^2)
- Can we store number -> [idx]

Trace [1 2 3 1]
- Check if 1 is in the map
    - Add 1 : [0]
- Check if 2 is in the map -> Add 2: [1]
- Check if 3 is in the map -> Add 3: [2]
- Check if 1 is in the map
    - Go through from behind and see if the abs difference is <= k

"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {} # nums[i] -> [i, i+1, ...]

        for i in range(len(nums)):
            if nums[i] not in mapping:
                mapping[nums[i]] = i
            else:
                # We only check the last idx found cause they'll have the smallest abs difference
                if abs(mapping[nums[i]] - i) <= k:
                    return True
                
                mapping[nums[i]] = i
        
        return False