class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2

            if target < matrix[mid][0]:
                high = mid - 1
            elif target > matrix[mid][-1]:
                low = mid + 1
            # This is the case where the number should be in the row    
            else:
                # We'll do a second binary search
                left, right = 0, len(matrix[mid]) - 1

                while left <= right:
                    middle = (left + right) // 2

                    if target < matrix[mid][middle]:
                        right = middle - 1
                    elif target > matrix[mid][middle]:
                        left = middle + 1
                    else:
                        return True

                return False
                
        return False
        