"""
Problem
- Pretty much the fib but with three numbers instead?

Cases:
0 = 0, 1 = 1, 2 = 1
trib[n] = trib[n-1] + trib[n-2] + trib[n-3]

Strategy:
- we can bottom up dp with 3 rolling variables
- t3 = 0, t2 = 1, t1 = 1
- temp = t3 + t2 + t1
- t3 = t2, t2 = t1, t1 = temp
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        
        # t3 = trib[n-3]
        t3, t2, t1 = 0, 1, 1 
        res = 0

        for i in range(3, n + 1):
            res = t3 + t2 + t1
            t3 = t2
            t2 = t1
            t1 = res
        
        return res
        