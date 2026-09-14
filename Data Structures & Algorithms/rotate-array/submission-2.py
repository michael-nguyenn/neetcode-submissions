class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        total_iterations = 0
        start = 0
        i = 0
        temp = nums[i]
        temp2 = nums[i]
        while total_iterations < len(nums):
            temp2 = nums[(i + k) % len(nums)]
            nums[(i + k) % len(nums)] = temp
            
            temp = temp2
            i = (i + k) % len(nums)
            total_iterations += 1 

            if total_iterations < len(nums) and start == i:
                start += 1
                i = start
                temp = nums[i]

        