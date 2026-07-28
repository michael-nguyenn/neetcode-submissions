class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            cur_area = min(heights[left], heights[right]) * width
            max_area = max(cur_area, max_area)

            # Move the min bounds with hopes of finding a larger
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


