class Solution 
{
public:
    vector<vector<int>> threeSum(vector<int>& nums) 
    {
        std::vector<std::vector<int>> res;

        // allows us to use two pointers if we sort
        std::sort(nums.begin(), nums.end());

        // now we go thru sorted nums, fix the first i and
        // use two pointers to see if left + right + i == 0
        int len = static_cast<int>(nums.size());
        for (int i = 0; i < len; i++)
        {
            // if the fixed element is the same as the last fixed element
            // we skip it (starting on i == 1)
            if (i != 0 and nums[i] == nums[i - 1]) { continue; }
            if (nums[i] > 0) { break; } // this is b/c there are no valid pairs left

            int left = i + 1;
            int right = len - 1;

            // we'll start just to the left and at the end
            while (left < right)
            {
                int cur_sum = nums[i] + nums[left] + nums[right];   
                // this means our sum is too large and we need to make it
                // smaller
                if (cur_sum > 0)
                {
                    right -= 1;
                }
                else if (cur_sum < 0)
                {
                    left += 1;
                }
                else
                {
                    res.push_back({nums[i], nums[left], nums[right]});

                    // at this point we need to move -> until it's not the same
                    // as the last value
                    left += 1;
                    while (left < right && nums[left] == nums[left - 1])
                    {
                        left += 1;
                    }
                }
            }

        }
        return res;
    }
};
