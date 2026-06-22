
class Solution 
{
public:
    string minWindow(const string& s, const string& t) 
    {
        std::unordered_map<char, int> t_freqs{};
        std::unordered_map<char, int> s_freqs{};
        int s_len = static_cast<int>(s.size());
        int left = 0;
        int right = 0;
        int need = 0;
        int have = 0;
        int res_len = s_len + 1;
        int res_left{};
        
        // we count the frequencies of each unique char in t
        for (const char c : t)
        {
            t_freqs[c] += 1;
        }

        // this specifies how many chars we have to satisfy inside our window
        need += static_cast<int>(t_freqs.size());

        // for the main loop, we will keep expanding --> while adding chars to s_freqs
        // anytime s_freqs[char] == t_freqs[char], we can increment have
        // if have == need, that means every character in t is present inside of our current
        // window (right - left + 1)
        // at this point we will start moving our left pointer -> as much as possible until
        // the window isn't valid anymore, each time we shrink we record and compare it to res
        while (right < s_len)
        {
            char cur_char = s[right];
            s_freqs[cur_char] += 1;
            if (t_freqs.contains(cur_char) && s_freqs[cur_char] == t_freqs[cur_char])
            {
                have += 1;
            }

            while (have == need)
            {
                // this is the case where we find a shorter substring than before
                if ((right - left + 1) < res_len)
                {
                    res_len = right - left + 1;
                    res_left = left;
                }

                s_freqs[s[left]] -= 1;
                if (t_freqs.contains(s[left]) && s_freqs[s[left]] < t_freqs[s[left]])
                {
                    have -= 1;
                }
                left++;
            }

            right++;
        }

        if (res_len == s_len + 1) { return ""; }
        else { return s.substr(res_left, res_len); } 
        
        
    }
};
