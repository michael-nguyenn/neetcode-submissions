class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int res{};
        std::unordered_set<int> unique_nums(nums.begin(), nums.end());

        for (const int num : unique_nums)
        {
            if (unique_nums.contains(num - 1)) { continue; }

            // Making it here means this num is currently the smallest of the sequence
            int seq_len = 1;
            int cur_num = num;
            while (unique_nums.contains(cur_num + 1))
            {
                seq_len += 1;
                cur_num += 1;
            }

            res = std::max(seq_len, res);
        }

        return res;
    }
};
