"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])

        rooms, res = 0, 0
        s_ptr, e_ptr = 0, 0

        while (s_ptr < len(start_times)):
            if start_times[s_ptr] < end_times[e_ptr]:
                rooms += 1
                s_ptr += 1
            else:
                rooms -= 1
                e_ptr += 1
            
            res = max(rooms, res)
        
        return res

        