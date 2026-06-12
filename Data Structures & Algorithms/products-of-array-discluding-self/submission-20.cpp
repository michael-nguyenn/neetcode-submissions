class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) 
    {
        int n = static_cast<int>(nums.size());
        std::vector<int> res(n);

        // same forward pass
        res[0] = 1;
        for (int i = 1; i < n; i++)
        {
            res[i] = res[i - 1] * nums[i - 1];
        }

        // fill out postfix on the backwards pass
        int postfix = 1;
        for (int i = n - 1; i >= 0; i--)
        {
            res[i] = res[i] * postfix;
            postfix = postfix * nums[i];
        }

        return res;

    }
};
