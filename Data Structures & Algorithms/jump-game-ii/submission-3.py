"""
Problem
- You're given an array where each i is how far to the right you can jump
- Your jump is 1 - nums[i] (you can jump up to the num at index i)
- i + j is within the bounds of nums.length
- Start at index 0 and goal is to reach the end with the smallest num of jumps

Cases
- Base Case is when you reach i == len(nums) - 1
    - Return 0
- If your jump i + j >= len(nums), then don't take that jump
- At any given index, you can jump between 1 - nums[i]
    - So if nums[i] == 0, then we're stuck and the ans is infinity
        - In 0 cases we should return infinity

Strategy
- Res variable set to infinity
- Starting from index i we attempt will jump from 1 - nums[i]
    - If legal jump then 
    - in each of the jumps, we res = min(res, 1 + dfs(i + j))

Trace
- index 0
    - res = infinity
    - take the first jump at 1, 1 + dfs(0 + 1)
    - receive 1 from dfs(0), and we can return res to the caller aka 2
- index 1
    - res = infinity
    - take the first jump at 1, 1 + dfs(1 + 1)
    - dfs(2) returns 3, we change res = 4 and we continue
    - take the second jump at 2, 1 + dfs(1 + 2), that hits the cache and returns 2, so now res becomes 3
    - take the third jump at 3, 1 + dfs(1 + 3), that hits the cache and returns 2, res becomes 2
    - take the fourth jump at 4, 1 + dfs(1 + 4), that hits the cache and returns 0, res becomes 1
    - that stores 1 at dfs(1), and returns 1 up to 0
- index 2
    - res = infinity
    - take the first jump at 1, 1 + dfs(2 + 1)
    - dfs(3) returns 2, we store away 3, and return 3
- index 3
    - res = infinity
    - take the first jump at 1, 1 + dfs(3 + 1)
    - dfs(4) returns 1, we do min(infinity, and 2)
    - store away 2, and return 2
- index 4
    - res = infinity
    - take the first jump at 1, 1 + dfs(4 + 1)
    - 0 is returned we do res = min(infinity, 1 + 0) = 1
    - then we can store away the 1 and return res 
- index 5
    - BASE CASE returns 0
"""  

class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {len(nums)-1:0}
    
        def dfs(i: int) -> int:
            if i in cache:
                return cache[i]
            
            res = float("infinity")
            for j in range(1, nums[i]+1):
                if i + j >= len(nums):
                    continue
                res = min(res, 1 + dfs(i + j))
            
            cache[i] = res
            return res

        return dfs(0)
        