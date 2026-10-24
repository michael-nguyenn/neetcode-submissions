import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_queries = sorted(queries) # creates a new copy
        res = {}
        intervals.sort() # in place sorting based on start time
        i = 0 # index of intervals        
        min_heap = []

        for query in sorted_queries:
            # find all intervals that start before and up to this query
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(min_heap, (end-start+1, end))
                i += 1
            
            # Clear out intervals that end before this one
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            res[query] = min_heap[0][0] if min_heap else -1
        
        return [res[i] for i in queries]