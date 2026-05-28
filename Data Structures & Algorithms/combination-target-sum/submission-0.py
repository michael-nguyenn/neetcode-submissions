class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, cur: List[int], total: int):
            # Base Cases
            if total == target:
                res.append(cur.copy())
                return
            
            # If we've run out of options or gone too high
            if i >= len(nums) or total > target:
                return
            
            # Otherwise we will add to cur and recurse
            cur.append(nums[i])
            dfs(i, cur, total + nums[i]) # we can include this number again

            # reaching here means we've explored all there is with i
            cur.pop()
            dfs(i + 1, cur, total) # now explore other options
        
        dfs(0, [], 0)
        return res