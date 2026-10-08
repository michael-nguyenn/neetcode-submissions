class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ROWS, COLS = n, n
        board = [["."] * n for _ in range(n)]
        res = []
        cols, pos_diags, neg_diags = set(), set(), set()

        def backtrack(row):
            if row == n:
                temp = []
                for r in range(ROWS):
                    temp.append("".join(board[r]))
                res.append(temp)
                return
            
            for c in range(COLS):
                if c in cols or (row + c) in pos_diags or (row - c) in neg_diags:
                    continue

                cols.add(c)
                pos_diags.add(row + c)
                neg_diags.add(row - c)
                board[row][c] = "Q"

                backtrack(row+1)

                cols.remove(c)
                pos_diags.remove(row + c)
                neg_diags.remove(row - c)
                board[row][c] = "."

        backtrack(0)
        return res
