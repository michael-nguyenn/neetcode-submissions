class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two_step = 0
        one_step = 0

        for i in range(len(cost)-1, -1, -1):
            cur = cost[i] + min(two_step, one_step)
            two_step = one_step
            one_step = cur
        
        return min(one_step, two_step)
        