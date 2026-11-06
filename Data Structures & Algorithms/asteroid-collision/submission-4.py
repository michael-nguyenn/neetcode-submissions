"""
Problem 
- asteroids[i] = asteroid, abs() is the size, otherwise sign is direction it's heading
    - + means going right, - means going left
- when two asteroids crash, 
    - the smallest one gets destroyed
    - same sized ones both get destroyed
- ones moving in the same direction will never collide


Example: [2, 4, -4, -1]
- indices represent their relative position
- 2, and 4 don't colide so we're ok
- 4 and -4 do colide, and that will break both
- 2 and -1 collide and -1 breaks

[2, -4, 4, -1]
- 2 and -4 crash, and 2 gets destroyed
- -4 and 4 never reach one another cause they travel at the same speed
- 4 and -1 do crash though and then -1 is destroyed

[7, -3, 9]
- 7 will collide with -3 and -3 breaks

[10, -1, -2, -3, 4, -4, -11]
- 10 eats up everything, then gets destroyed by 11 

Strategy
- asteroids will collide if their positive -> is before negative <-
- if negative is in front <-, positive goes -> so they don't collide
- same signs also don't collide
- As we go thru asteroids, we start adding positive elements to a stack
- Upon hitting a negative asteroid, we pop from the stack and start destroying
    - If stack[-1] is > asteroid[i], then asteroid[i] is destroyed
    - If stack[-1] is < asteroid[i], then stack[-1] is destroyed, we pop and continue with the next element in the stack
    - If they're the same, then they're both destroyed, we pop from the stack and move onto next i
    - In the scenario where our stack is empty then asteroid[i] will never be destroyed
    - At the end we should append whatever is left in stack
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        res = []

        i = 0
        while i < len(asteroids):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
                i += 1
            else:
                destroyed = False
                while stack:
                    if stack[-1] > abs(asteroids[i]):
                        destroyed = True          # this asteroid breaks
                        break
                    elif stack[-1] < abs(asteroids[i]):
                        stack.pop()               # top breaks, keep checking
                    else:
                        stack.pop()               # both break
                        destroyed = True
                        break

                # stack ran out without destroying it
                if not destroyed:
                    res.append(asteroids[i])
                i += 1
        
        return res + stack

