class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // set to store duplicates
        std::unordered_set<int> seen;

        // loop through the nums vector
        for (auto num : nums)
        {
            // if this element exists in the set then we return false
            if (seen.count(num) == 1) {
                return true;
            }

            // otherwise add it to the set
            seen.insert(num);
        }

        // return true
        return false;
    }
};