// we start two pointers on the same character and advance right pointer on
// every iteration trying to expand our substring, while recording the length and seen set
// anytime we run into a character that's already in our set it means that 
// our substring is no longer valid and we must advance left to where right is 

class Solution 
{
public:
    int lengthOfLongestSubstring(const string s) 
    {
        int s_len = static_cast<int>(s.size());
        if (s_len == 0) { return 0; }

        std::unordered_set<char> seen;
        int left = 0;
        int right = 0;
        int res = 0;

        while (right < s_len)
        {
            // we have to check if the cur char is in our window already
            while(seen.contains(s[right])) 
            {
            // then we must move stepwise and remove all characters up until the duplicate
                seen.erase(s[left]);
                left++;

            }

            // add to the set and advance
            seen.insert(s[right]);
            res = std::max(res, (right - left + 1));
            right++;
        }
        return res;
    }
};
