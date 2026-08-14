class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.divide(nums, 0, len(nums) - 1)
        return nums
    
    def divide(self, nums, left, right):
        if left >= right:
            return
        
        mid = (left + right) // 2
        # Divide the left & right
        self.divide(nums, left, mid)
        self.divide(nums, mid + 1, right)

        # Then merge the two halves
        self.merge(nums, left, mid, right)
        
    def merge(self, nums, left, mid, right):
        left_arr = nums[left:mid+1]
        right_arr = nums[mid+1:right+1]

        cur, l_p, r_p = left, 0, 0

        # Go thru each half and merge
        while l_p < len(left_arr) and r_p < len(right_arr):
            if left_arr[l_p] < right_arr[r_p]:
                nums[cur] = left_arr[l_p]
                l_p += 1
            else:
                nums[cur] = right_arr[r_p]
                r_p += 1
            
            cur += 1
        
        # Then we'll drain the remaining half
        # One of these will run
        while l_p < len(left_arr):
            nums[cur] = left_arr[l_p]
            l_p += 1
            cur += 1
            
        while r_p < len(right_arr):
            nums[cur] = right_arr[r_p]
            r_p += 1
            cur += 1

