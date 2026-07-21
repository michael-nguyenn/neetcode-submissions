class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(row, col) -> None:
            if row < 0 or col < 0 or row == ROWS or col == COLS:
                return
            
            if board[row][col] == 'X' or board[row][col] == 'M':
                return

            board[row][col] = 'M'

            for r, c in directions:
                dfs(row + r, col + c)


        for row in range(ROWS):
            for col in range(COLS):
                if (row in (0, ROWS - 1) or col in (0, COLS - 1)) and board[row][col] == 'O':
                    dfs(row, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'M':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'

                