class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []

        def backtrack():
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack()
                    path.pop()
        
        backtrack()
        return res
        