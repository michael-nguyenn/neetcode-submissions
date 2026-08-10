class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The maximum k will be bound by the largest pile within piles.
        # That is the fastest eating rate we actually need to eat
        max_rate = max(piles) # O(n)
        res = max_rate
        
        # We'll do a binary range search in the range of 1, max_rate
        # if we find our eating rate is satisfies the given hours, we'll
        # try to find a slower rate that still satisfies the hours
        left, right = 1, max_rate
        while left <= right:
            mid = (left + right) // 2
            current_time = self.get_hours(piles, mid)
            if current_time <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return res
    
    def get_hours(self, piles, k) -> int:
        hours = 0
        for i in range(len(piles)):
            hours += math.ceil(piles[i] / k)
        return hours

