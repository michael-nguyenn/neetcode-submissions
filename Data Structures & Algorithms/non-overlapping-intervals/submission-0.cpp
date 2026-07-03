class Solution 
{
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) 
    {
        int len = static_cast<int>(intervals.size());
        std::sort(intervals.begin(), intervals.end());
        int end_bound = intervals[0][1];
        int res = 0;

        for (int i = 1; i < len; i++)
        {
            int start = intervals[i][0];
            int end = intervals[i][1];

            // if the current interval comes after our end_bound
            if (start >= end_bound)
            {
                end_bound = end;
            }
            else
            {
                res++;
                end_bound = std::min(end_bound, end);
            }
        }

        return res;
        
    }
};
