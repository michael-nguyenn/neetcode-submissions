// We'll use a heap + lazy delete to maintain an ordering
// on our window.

class Solution 
{
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) 
    {
        std::vector<int> res;
        std::priority_queue<std::pair<int, int>> max_heap;
        std::unordered_set<int> removed_set;

        for (int i = 0; i < k; i++)
        {
            max_heap.push({nums[i], i});
        }
        res.push_back(max_heap.top().first);

        int len = static_cast<int>(nums.size());
        for (int i = 0; i < len - k; i++)
        {
            int ele_to_add = nums[i + k];

            max_heap.push({ele_to_add, i + k});
            removed_set.insert(i);

            // Make sure our top element didn't get removed
            while (removed_set.contains(max_heap.top().second))
            {
                max_heap.pop();
            }

            res.push_back(max_heap.top().first);
        }

        return res;
    }
};
