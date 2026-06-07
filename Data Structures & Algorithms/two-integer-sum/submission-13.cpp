class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // need a unordered map mapping num (int) to index (int)
        std::unordered_map<int, int> indices{};

        // go through the vector of nums (without modifying)
        for (auto i = 0; i < nums.size(); i++)
        {
            // need to check if target - nums[i] is in our unordered map
            int difference = target - nums[i];

            if (indices.find(difference) != 0)
            {
                // if it is, then we can return a vector of the two indices (smallest index)
                return {indices[difference], i};

            }
                
            // otherwise we'll add the entry to the map
            indices[nums[i]] = i;

        }
        return {};
    }
};
