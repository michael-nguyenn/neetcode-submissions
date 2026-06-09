class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::vector<int> res;

        // need to create a map of num -> freq
        std::unordered_map<int, int> freqs;

        for (const auto& num : nums) 
        {
            freqs[num] += 1;
        }

        // then we have to create a min heap and maintain size k
        std::priority_queue<
            std::pair<int,int>, 
            std::vector<std::pair<int,int>>, 
            std::greater<std::pair<int,int>>
        > min_h;

        // we need to push a pair<freq,num> onto the heap
        for (auto& [num, freq] : freqs)
        {
            min_h.push(std::make_pair(freq, num));

            // if our heap passes k then we pop
            if (min_h.size() > k)
            {
                min_h.pop();
            }
        }

        // now we can pop k times, and append to res
        for (int i = 0; i < k; i++)
        {
            res.push_back(min_h.top().second);
            min_h.pop();
        }
        return res;
    }
};
