class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> groups{};
        std::vector<std::vector<string>> res;

        for (const auto& str : strs)
        {
            std::string sorted_str = str;
            std::sort(sorted_str.begin(), sorted_str.end());

            groups[sorted_str].push_back(str);
        }

        for (const auto& group : groups)
        {
            res.push_back(group.second);
        }

        return res;
    }
};
