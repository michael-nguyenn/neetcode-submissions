"""
Problem
You're given a string of 0s and 1s, you want to split it into two. In the left only zeros count towards your score, and in the right only 1s count towards your score

Example 0 0 1 1 1
- 0, 0111 -> 1 + 3 = 4
- 00, 111 -> 2 + 3 = 5
- 001, 11 -> 2 + 2 = 4
- 0011, 1 -> 2 + 1 = 3

Strategy
- Need a res
- So we start a split at idx 1 so that we can read s[0]
- want to end at len(s) - 1, so that we can read s[-1]
- prefix sum to count the number of 1s at a given index?

 0 1 2 3 4 5
[0 1 2 3 3 4]

 0 1 2 3 4 5
[1 1 1 1 2 2]

Complexity
O(n) for time and space
"""

class Solution:
    def maxScore(self, s: str) -> int:
        ones, zeros = [0] * len(s), [0] * len(s)
        res = 0

        one_sum, zero_sum, = 0, 0
        for i in range(len(s)):
            if s[i] == '0':
                zero_sum += 1
            else:
                one_sum += 1
            
            ones[i] = one_sum
            zeros[i] = zero_sum
        
        for i in range(1, len(s)):
            res = max(res, zeros[i-1] + (ones[-1] - ones[i-1]))

        return res

        