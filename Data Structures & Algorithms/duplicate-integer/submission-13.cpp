class Solution {
public:
    bool hasDuplicate(const vector<int>& nums) {
        // set to store duplicates
        std::unordered_set<int> seen;

        // loop through the nums vector
        for (const auto& num : nums)
        {
            // if this element exists in the set then we return false
            if (seen.contains(num)) {
                return true;
            }

            // otherwise add it to the set
            seen.insert(num);
        }

        // return true
        return false;
    }
};