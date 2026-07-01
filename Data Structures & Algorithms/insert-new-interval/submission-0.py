class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
	
	
        for i in range(len(intervals)):
            # if new interval comes before all other intervals
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # new interval slots in after the current interval
            elif newInterval[0] > intervals[i][1]:
                # so then we append the interval and move onto the next 
                res.append(intervals[i])
            # this means there is an overlap
            # the lower bound of new interval is <= intervals[i][1] 
            else:
                # merge
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        # here it means that after all the merging, newInterval is 
        # the largest non overlapping interval
        res.append(newInterval)
        return res