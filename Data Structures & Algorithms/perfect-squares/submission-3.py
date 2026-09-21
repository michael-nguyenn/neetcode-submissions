class Solution:
    def numSquares(self, n: int) -> int:
        p_squares = []

        for i in range(1, n + 1):
            p_square = i * i

            if p_square > n:
                break
            
            p_squares.append(p_square)

        
        dp = [math.inf for i in range(n + 1)]
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            for square in p_squares:
                if i + square > n:
                    continue

                dp[i] = min(dp[i], 1 + dp[i + square])
        
        return dp[0]





        