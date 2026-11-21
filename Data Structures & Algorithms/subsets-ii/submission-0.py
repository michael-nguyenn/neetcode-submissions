"""
Problem
- Given an unsorted array of duplicate integers, have to return unique subsets in any order

Trace [1,1,2]
backtrack(0)
- take 1 -> [1]
    backtrack(1)
    - take 1 -> [1,1]
        backtrack(2)
        - take 2 -> [1,1,2]
            backtrack(3)
            -> base case, append [1,1,2]
        - pop 2 -> [1,1]
        - consider the ignore case
            backtrack(3)
            -> base case, append [1,1]
        -> return
    - pop 1 -> [1]
    - consider the ignore case
        backtrack(2)
        - take 2 -> [1,2]
            backtrack(3)
            -> base case, append [1,2]
        - pop 2 -> [1]
        - consider the ignore case
            backtrack(3)
            -> base case, append [1]
        -> return
    -> return
- pop 1 -> []
- consider the ignore case, while i+1 == i, skip that index, skip 1
    backtrack(2)
    - take 2 -> [2]
        backtrack(3)
        -> base case, append [2]
    - pop 2 -> []
    - consider ignore case
        backtrack(3)
        -> base case, append []
    -> return
-> return
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                res.append(path.copy())
                return

            # taken path
            path.append(nums[i])
            backtrack(i+1)
            path.pop()

            # ignore path
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)
        
        backtrack(0)
        return res

        