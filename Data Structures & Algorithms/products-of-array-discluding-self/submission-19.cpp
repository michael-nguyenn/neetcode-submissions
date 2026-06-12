class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) 
    {
        int n = static_cast<int>(nums.size());
        std::vector<int> prefix(n);
        std::vector<int> postfix(n);
        std::vector<int> res(n);
        

        prefix[0] = 1;
        postfix[nums.size() - 1] = 1;

        for (int i = 1; i < n; i++)
        {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        for (int i = n - 2; i >= 0; i--)
        {
            postfix[i] = postfix[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < n; i++)
        {
            res[i] = prefix[i] * postfix[i];
        }

        return res;
    }
};
