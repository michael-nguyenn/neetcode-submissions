// after an array gets sorted, we are left with two sorted halves
// the left side contains elements greater than the right side
// the smallest element lives as the first element of the right side

// we can determine if we're on the left side by seeing if nums[mid] >= nums[left]
// then we search -> by moving left 
// if we're on the right side we move right <- to potentially find a smaller element
// if we ever get to the scenario where left < right then we're in a fully sorted portion
// and we can simply return nums[left]

class Solution 
{
public:
    int findMin(vector<int> &nums) 
    {
        int len = static_cast<int>(nums.size());
        int left = 0, right = len - 1, res = nums[0];

        while (left <= right)
        {
            // edge case
            if (nums[left] < nums[right]) 
            { 
                res = std::min(nums[left], res);
                break;
            }

            int mid = left + (right - left) / 2;
            res = std::min(nums[mid], res);


            if (nums[mid] >= nums[left])
            {
                left = mid + 1;
            } 
            else
            {
                right = mid - 1;
            }
        }
        return res;
    }
};
