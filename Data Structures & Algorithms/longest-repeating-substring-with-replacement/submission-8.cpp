// a valid window is len of window (r - l + 1) - most freq char <= k
// this is b/c we have to keep the difference between window and most freq char
// to up to k amounts, that's how many chars we're allowed to replace

// pointers start together, the right pointer adds chars to a hash map
// each iteration we go thru the hashmap and get the value of the highest occuring char
// this costs up to O(26) per iteration -> O(1)
// if our window ever goes invalid, we can move our left pointer forward once to make it
// a valid window again

// runs in O(n) time and O(1) space

class Solution 
{
public:
    int characterReplacement(string s, int k) 
    {
        int len = static_cast<int>(s.size());
        std::array<int, 26> freqs{};
        int left = 0;
        int right = 0;
        int res = 1; // string will never be empty

        while (right < len)
        {
            // increment the frequencies
            int cur_max = 0;
            freqs[s[right] - 'A'] += 1;
            for (int i = 0; i < 26; i++)
            {
                cur_max = std::max(freqs[i], cur_max);
            }
            
            // then check if we violate our window
            if ((right - left + 1) - cur_max > k)
            {
                freqs[s[left] - 'A'] -= 1;
                left++;
            }

            res = std::max((right - left + 1), res);
            right++;
        }
        return res;
    }
};
