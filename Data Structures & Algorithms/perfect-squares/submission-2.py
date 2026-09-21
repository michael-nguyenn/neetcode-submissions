import sys
sys.setrecursionlimit(10**6)

class Solution:
    def numSquares(self, n: int) -> int:
        p_squares = []

        for i in range(1, n + 1):
            p_square = i * i

            if p_square > n:
                break
            
            p_squares.append(p_square)

        cache = {n: 0}

        # returns the min number of perfect squares to sum to n
        def dfs(total: int) -> int:
            if total in cache:
                return cache[total]
            
            if total > n:
                return math.inf

            min_num = math.inf

            for num in p_squares:
                min_num = min(min_num, 1 + dfs(total + num))
            
            cache[total] = min_num
            return min_num
        
        return dfs(0)


