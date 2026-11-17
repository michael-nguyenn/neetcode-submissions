"""
Problem
- return all possible subsets of an array
- we can either include or skip this number

Example
[1,2,3]
-                   [] | [1]
    -          [], [2] | [1], [1,2]
  [], [3] | [2], [2,3] | [1], [1,3] | [1,2], [1,2,3]

"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i:int, subset: List[int]) -> None:
            if i == len(nums):
                res.append(subset.copy())
                return
            
            backtrack(i+1, subset) # don't include the cur

            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
        
        backtrack(0, [])
        return res

        