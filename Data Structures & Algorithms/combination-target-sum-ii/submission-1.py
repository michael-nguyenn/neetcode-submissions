class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur_path = [], []
        candidates.sort()

        def backtrack(i, total):
            if total == target:
                res.append(cur_path.copy())
                return
            if i == len(candidates) or total > target:
                return
            
            # Take path
            cur_path.append(candidates[i])
            backtrack(i+1, total+candidates[i])
            cur_path.pop()

            # Ignore path
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, total)
        
        backtrack(0, 0)
        return res
        