class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS, COLS = len(matrix), len(matrix[0])
        first_row = False

        # First pass is we're seeing which row/col needs to be zeroed out
        for row in range(ROWS):
            for col in range(COLS):
                # if the current cell is a 0, we mark the corresponding embeded array
                if matrix[row][col] == 0:
                    # the columns array sits on row zero
                    matrix[0][col] = 0

                    # the rows array sits on the first column, except the first row
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        first_row = True # this accounts for the overlap

        # Second pass: Zero out stuff below our embeded markers
        for row in range(1, ROWS):
            for col in range(1, COLS):
                # We refer to our embeded arrays to see if they were marked 0
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        # Final Pass is to potentially zero out the first row and the first column
        if matrix[0][0] == 0: # represents the first column
            for row in range(ROWS):
                matrix[row][0] = 0

        if first_row:
            for col in range(COLS):
                matrix[0][col] = 0
