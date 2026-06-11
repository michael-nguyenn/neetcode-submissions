class Solution 
{
public:

    string encode(vector<string>& strs) 
    {
        std::string s;

        for (const auto& str : strs)
        {
            size_t s_len = str.size();
            s += std::to_string(s_len);
            s += '#';
            s += str;
        }
        return s;
    }

    vector<string> decode(string s) 
    {
        std::vector<std::string> res;
        size_t beg = 0;
        while (beg < s.size())
        {
            size_t delim_idx = s.find('#', beg);
            size_t len = std::stoi(s.substr(beg, delim_idx - beg));
            res.push_back(s.substr(delim_idx + 1, len));
            beg = delim_idx + len + 1; 
        }
        return res;
    }
};
