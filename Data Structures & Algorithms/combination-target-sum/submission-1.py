class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, cur_path, total):
            if idx >= len(nums) or total > target:
                return

            if total == target:
                res.append(list(cur_path))
                return

            # we either include the cur number again or not
            cur_path.append(nums[idx])
            dfs(idx, cur_path, total + nums[idx])
            cur_path.pop()

            # once we explore the including number again we move on
            dfs(idx + 1, cur_path, total)

        dfs(0, [], 0)
        return res
            

             
        