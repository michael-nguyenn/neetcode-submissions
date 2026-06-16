class Solution 
{
public:
    bool isPalindrome(const string& s) 
    {
        // need two pointers one at the start and one at the end
        int left = 0;
        int right = s.size() - 1;

        // go until the two pointers meet, so left < right
        // for odd len strings it will meet in the middle = valid
        // for even len strings it will cross = valid
        while (left < right)
        {
            // we need to skip over non alphanumeric chars
            while (left < right && !std::isalnum(static_cast<unsigned char>(s[left])))
            {
                left ++;
            }

            while (right > left && !std::isalnum(static_cast<unsigned char>(s[right])))
            {
                right --;
            }

            // then we convert to lower case and compare
 
            char left_lowered = std::tolower(static_cast<unsigned char>(s[left]));
            char right_lowered = std::tolower(static_cast<unsigned char>(s[right]));

            if (left_lowered != right_lowered) 
            {
                return false;
            }

            left += 1;
            right -= 1;
        }

        return true;
    }
};
