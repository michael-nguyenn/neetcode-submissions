class Solution {
public:
    bool isAnagram(string s, string t) 
    {

        // each index of the array represents a-z where
        // counts[0] = a and counts[25] = z
        std::array<int, 26> counts; 

        // we'll loop through each string increment for one
        // decrement for the other
        for (char c : s) { counts[c - 'a']++; }

        for (char c : t) { counts[c - 'a']--; }

        // then loop through it one more time to see if all entries are 0
        for (int count : counts)
        {
            if (count != 0) { return false; }
        }
        return true;
    }
};
