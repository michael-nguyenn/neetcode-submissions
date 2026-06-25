// left half is going to be greater than the right half
// we can tell if we're in the left half by mid >= left
// if we're in the left side of the array then we can see if
// our target is within the bounds of our left side.
// if target < left or target > mid, that means we should search -->

class Solution 
{
public:
    int search(vector<int>& nums, int target) 
    {
        int nums_len = static_cast<int>(nums.size());
        int left = 0, right = nums_len - 1;

        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) { return mid; }

            // now we have to determine which half we're in
            if (nums[mid] >= nums[left])
            {
                if (target < nums[left] || target > nums[mid])
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid - 1;
                }
            }
            // this is if we're in the right half
            else
            {
                if (target > nums[right] || target < nums[mid])
                {
                    right = mid - 1;
                }
                else
                {
                    left = mid + 1;
                }
            }
        }
        return -1;
    }
};
