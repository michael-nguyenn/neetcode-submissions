class Solution 
{
public:
    int maxArea(const vector<int>& heights) 
    {
        int len = static_cast<int>(heights.size());
        int left = 0;
        int right = len - 1;
        int res{};

        // want to move pointers before they cross
        while (left < right)
        {
            int container_bound = std::min(heights[left], heights[right]);
            int cur_water = container_bound * (right - left);
            res = std::max(cur_water, res);

            // now we update our pointers
            if (heights[left] <= heights[right]) { left++; }
            else { right--; }
        }

        return res;
    }
};
