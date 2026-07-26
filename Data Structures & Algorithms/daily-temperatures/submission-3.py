# Stack contains all temperatures along with their positions in temperatures 
# in monotonic decreasing order.
# Anytime we find a new daily temperature that is higher than our old temp at the 
# top of our stack, we can pop it. The difference in idices is the amount of days
# between the two temperatures.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack: list[tuple[int, int]] = [] # temp, index

        for i, cur_temp in enumerate(temperatures):
        
            while stack and stack[-1][0] < cur_temp:
                t, idx = stack.pop()
                res[idx] = i - idx
            
            stack.append((cur_temp, i))

        return res


        