class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = right # we're gonna try and maximize this

        while left <= right:
            mid = (left + right) // 2
            
            cur_days = self.get_days(mid, weights)
            if cur_days <= days:
                right = mid - 1
                res = min(mid, res)
            else:
                left = mid + 1
        
        return res


    def get_days(self, capacity, weights) -> int:
        cur_capacity, cur_days = capacity, 1

        for weight in weights:
            if cur_capacity - weight < 0:
                # increment days
                cur_days += 1
                cur_capacity = capacity - weight

            else:
                cur_capacity -= weight

        return cur_days


        
        