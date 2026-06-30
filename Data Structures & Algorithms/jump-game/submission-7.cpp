class Solution 
{
public:
    bool canJump(vector<int>& nums) 
    {
        int num_len = static_cast<int>(nums.size());
        int goal = num_len - 1;

        // then we have to go backwards
        for (int i = num_len - 1; i >= 0; i--)
        {
            if (i + nums[i] >= goal)
            {
                goal = i;
            }
        }

        return goal == 0;
        
    }
};
