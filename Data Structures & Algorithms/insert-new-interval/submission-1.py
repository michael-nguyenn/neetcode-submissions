class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        cur_start, cur_end = newInterval

        for i in range(len(intervals)):
            start, end = intervals[i]
            # This is if the cur_interval comes before interval
            if cur_end < start:
                res.append([cur_start, cur_end])
                return res + intervals[i:]
            # This is if cur_interval comes after interval
            elif cur_start > end:
                res.append([start, end])
            # This is if we have an overlap
            else:
                cur_start = min(cur_start, start)
                cur_end = max(cur_end, end)
        
        res.append([cur_start, cur_end])
        return res

            
        