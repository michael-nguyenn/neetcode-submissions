class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left, right = 0, len(heights) - 1

        while left < right:
            cur_area = min(heights[left], heights[right]) * (right - left)
            res = max(cur_area, res)

            # Figure out which pointer to update
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
            
        return res