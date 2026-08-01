class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [] # (idx, height)

        for i, height in enumerate(heights):
            left_bound = i
            
            # while the stack is non empty and
            # the top element's height is > current height
            while stack and stack[-1][1] > height:
                # we remove the element, calculate its area and update left_bound
                idx, h = stack.pop()
                res = max(res, h * (i - idx))
                left_bound = idx
            
            stack.append((left_bound, height))
        
        # What's remaining in the stack at this point are all the rectangles that
        # can be extended to the end
        while stack:
            idx, h = stack.pop()
            res = max(res, h * (len(heights) - idx))
        
        return res
        