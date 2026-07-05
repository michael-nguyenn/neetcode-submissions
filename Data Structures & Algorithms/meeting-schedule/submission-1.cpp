/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution 
{
public:
    bool canAttendMeetings(vector<Interval>& intervals) 
    {
        int len = static_cast<int>(intervals.size());
        // zero and one interval are always ok
        if (len < 2) { return true; }

        auto cmp = [](const Interval& a, const Interval& b) 
        {
            if (a.start != b.start) { return a.start < b.start; }
            else { return a.end < b.end; }
        };
        std::sort(intervals.begin(), intervals.end(), cmp);

        // we want to go thru all the intervals and ensure there is no overlap
        // and overlap would be int1's end is > int2's begin
        for (int i = 0; i < len - 1; i++)
        {
            Interval first = intervals[i];
            Interval second = intervals[i + 1];

            if (first.end > second.start)
            {
                return false;
            }
        }

        return true;
    }
};
