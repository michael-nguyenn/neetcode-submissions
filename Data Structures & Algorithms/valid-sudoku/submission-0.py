class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key (row // 3, col // 3)

        # Then we can go through each number on the board
        for row in range(9):
            for col in range(9):
                # Ignore the '.'
                if board[row][col] == ".":
                    continue

                # Then we'll check the respective set in the dict
                value = board[row][col]

                # rows[row] contains a set of numbers at that particular row
                # cols[col] contains a set of numbers at that particular column
                if (value in rows[row] or 
                    value in cols[col] or 
                    value in squares[(row // 3, col // 3)]):
                    return False

                # If we've made it here, it means the value wasn't in any of the dicts
                rows[row].add(value)
                cols[col].add(value)
                squares[(row//3, col//3)].add(value)

        
        # Making it here means our board is valid
        return True