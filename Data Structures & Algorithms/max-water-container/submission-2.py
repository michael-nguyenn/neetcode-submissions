class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        # Go until the second last element
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                cur_area = min(heights[i], heights[j]) * (j - i)
                res = max(cur_area, res)
        
        return res


        