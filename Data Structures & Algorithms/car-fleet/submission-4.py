# 7 -> 3 turns
# 5 -> (10 - 5) / 2 -> 2.5 turns
# 1 -> 10 - 1 / 2 -> 5 turns
# 0 -> (10 - 0) / 1 -> 10 turns

# we can sort by position [0,1,4,7]
# probably need to attach the turns as well

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        res = 0

        # O(n)
        for i in range(len(position)):
            pos = position[i]
            spd = speed[i]
            stack.append((pos, ((target - pos) / spd)))
        
        stack.sort()

        # At most O(n)
        while stack:
            res += 1
            _, turns = stack.pop()

            while stack and stack[-1][1] <= turns:
                stack.pop()

        return res