class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ROWS, COLS = n, n
        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(row):
            if row == n:
                temp = []
                for r in range(ROWS):
                    temp.append("".join(board[r]))
                res.append(temp)
                return
            
            for c in range(COLS):
                if self.check(row, c, board, ROWS, COLS):
                    board[row][c] = "Q"
                    backtrack(row+1)
                    board[row][c] = "."

        backtrack(0)
        return res


    def check(self, row, col, board, ROWS, COLS):
        # Horizontal Check
        for i in range(COLS):
            if i == col:
                continue
            if board[row][i] == "Q":
                return False
        # Vertical Check
        for i in range(ROWS):
            if i == row:
                continue
            if board[i][col] == "Q":
                return False 
        #  Main Diagonal Check
        r, c = row+1,col+1
        while r < ROWS and c < COLS:
            if board[r][c] == "Q":
                return False
            r += 1
            c += 1
        
        r, c = row-1,col-1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        
        # Oposite Diagonal Check
        r, c = row+1, col-1
        while r < ROWS and c >= 0:
            if board[r][c] == "Q":
                return False
            r += 1
            c -= 1
        
        r, c = row-1, col+1
        while c < COLS and r >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
        
        return True


        