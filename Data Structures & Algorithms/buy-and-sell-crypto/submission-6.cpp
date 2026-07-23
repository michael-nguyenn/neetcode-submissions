class Solution 
{
public:
    int maxProfit(vector<int>& prices) 
    {
        int res = 0;
        size_t left = 0, right = 0;
        while(right < prices.size())
        {
            if (prices[right] < prices[left])
            {
                left = right;
            }

            res = std::max((prices[right] - prices[left]), res);

            right++;
        }
        return res;   
    }
};
