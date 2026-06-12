class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) 
    {
        std::vector<int> prefix;
        prefix.resize(nums.size());
        std::vector<int> postfix;
        postfix.resize(nums.size());
        std::vector<int> res;
        res.resize(nums.size());

        prefix[0] = 1;
        postfix[nums.size() - 1] = 1;

        for (int i = 1; i < nums.size(); i++)
        {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        for (int i = nums.size() - 2; i >= 0; i--)
        {
            postfix[i] = postfix[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < nums.size(); i++)
        {
            res[i] = prefix[i] * postfix[i];
        }

        return res;
    }
};
