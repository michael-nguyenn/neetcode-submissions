"""
Problem
- Given an array of integers, must return a list of unique combinations
- A combination is just a subset of candidates that = target

Strategy
1,1,1,2 target = 2
output = 1,1 | 2

- How to deal with duplicates?
    - Deal wit duplicates in the skip branch
- Sort the array so duplicates are next to one another [1,2,2,4,5,6,9]
- Base cases are
    - If we == target
    - If we surpass target
    - If we're at the end of our array
- For every index i in candidates we can
    - Skip the current i -> call backtrack(i+1, total)
    - Include the current i -> call backtrack(i+1, total+candidates[i])

Trace [1,1,1,2] target = 2
backtrack(0, 0)
- take 1 [1]
    backtrack(1, 1)
    - take 1 [1,1]
        backtrack(2, 2)
        -> base case, append [1,1]
    - pop 1 [1]
    - consider the ignore case
    - while i < len(candidates), skip if i == i+1
        backtrack(3, 1)
        - take 2 [1,2]
            backtrack(4, 3)
            -> base case, do not append
        - pop 2 [1]
        - consider ignore case
            backtrack(4, 1)
            -> base case, do not append
        -> return
    -> return
- pop 1 []
- consider ignore case
- while i < len(candidates), skip if i == i+1
- 0 == 1, 1 == 2, 2 != 3
backtrack(3, 0)
- take 2 [2]
    backtrack(4, 2)
    -> base case, append [2]
- pop 2 []
-> return
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur_path = [], []
        candidates.sort()

        def backtrack(start, total):
            if total > target:
                return
            if total == target:
                res.append(cur_path.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                cur_path.append(candidates[i])
                backtrack(i+1, total+candidates[i])
                cur_path.pop()
        
        backtrack(0, 0)
        return res
            

        