"""
Problem
- Without using a built in library computer x^n
    - 3^5 is 3x3x3x3x3

Strategy
- Brute force would be looping n times and multiplying x by itself n times (starting x at 1)
- We can make this algorithm log(n) by spliting up like
    - 3^6 = 3^3 * 3^3 = (3^1 * 3^1 * 3^1) * (3^1 * 3^1 * 3^1) 

Cases
- when n == 0, then we return 1
- when the current frame has an odd exponent, then we multiple once more.
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            # if x == 0:
            #     return 0
            if n == 0:
                return 1        
            
            res = helper(x, n//2)
            res *= res

            if n % 2 != 0:
                res *= x
            
            return res
        
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
        