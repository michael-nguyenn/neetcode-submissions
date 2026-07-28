class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = 0

        # Determine how many turns each car takes to arrive to the target
        stack = []

        for i in range(len(position)):
            turns = (target - position[i]) / speed[i]
            stack.append((position[i], turns))


        # Sort it our stack based on original position
        stack.sort()

        # Now we'll pop on element at a time and try to form as many
        # fleets as needed
        while stack:
            _, turns = stack.pop()
            fleets += 1

            while stack and stack[-1][1] <= turns:
                stack.pop()

        return fleets