class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(board), len(board[0])
        found = False

        def find_word(row: int, col: int, word_index: int) -> bool:
            nonlocal found
            # Base Cases
            if found or word_index == len(word):
                found = True
                return True

            if (row == ROWS or col == COLS) or (row < 0 or col < 0) or (row, col) in visited:
                return False

            # Now we can see if adding this word completes
            if  board[row][col] == word[word_index]:
                visited.add((row, col))

                for r, c in directions:
                    if find_word(row + r, col + c, word_index + 1):
                        return True

                visited.remove((row, col))
            
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if find_word(i, j, 0):
                        return True
            
        return False
