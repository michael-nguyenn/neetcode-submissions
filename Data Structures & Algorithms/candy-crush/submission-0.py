class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(board), len(board[0])
        to_crush = set()

        def find(row, col):
            horizontal = []
            vertical = []

            for i in range(0, ROWS - row):
                if board[row][col] == board[row+i][col]:    
                    vertical.append((row+i, col))
                else:
                    break 

            for i in range(0, COLS - col):
                if board[row][col] == board[row][col+i]:    
                    horizontal.append((row, col+i))
                else:
                    break

            if len(horizontal) >= 3:
                for cell in horizontal:
                    to_crush.add(cell)

            if len(vertical) >= 3:
                for cell in vertical:
                    to_crush.add(cell)  

        def crush(to_crush):
            for r,c in to_crush:
                board[r][c] = 0
            
            to_crush.clear()

        def drop():
            # now we have to find the lowest 0 in each column
            for c in range(COLS):
                lowest_zero = -1

                # Iterate over each column
                for r in range(ROWS - 1, -1, -1):
                    if board[r][c] == 0:
                        lowest_zero = max(lowest_zero, r)

                    # Swap current non-zero candy with the lowest zero.
                    elif lowest_zero >= 0:
                        board[r][c], board[lowest_zero][c] = board[lowest_zero][c], board[r][c]
                        lowest_zero -= 1    

        while True:                
            for row in range(ROWS):
                for col in range(COLS):
                    if board[row][col] == 0:
                        continue
                        
                    find(row, col)
            
            if len(to_crush) == 0:
                break

            crush(to_crush)
            drop()

        return board 

