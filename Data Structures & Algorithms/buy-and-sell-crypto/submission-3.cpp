class Solution {
public:
    int maxProfit(vector<int>& prices) 
    {
        int len = static_cast<int>(prices.size());
        int res = 0;
        int left = 0;
        int right = 1;

        while (right < len)
        {
            if (prices[left] > prices[right])
            {
                left = right;
            }

            res = std::max(res, prices[right] - prices[left]);
            right++;
        }

        return res;
        
    }
};
