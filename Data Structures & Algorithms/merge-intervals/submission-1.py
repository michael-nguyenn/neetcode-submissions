class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        cur_interv = intervals.pop(0)
        res = []
        print(cur_interv)
        print(intervals)

        for i in range(len(intervals)):
            if cur_interv[1] < intervals[i][0]:
                res.append(cur_interv)
                cur_interv = intervals[i]
            else:
                cur_interv[0] = min(cur_interv[0], intervals[i][0])
                cur_interv[1] = max(cur_interv[1], intervals[i][1])
        
        res.append(cur_interv)
        return res