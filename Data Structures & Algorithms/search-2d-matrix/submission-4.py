class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                print("here")
                # Normal Binary Search
                left, right = 0, len(matrix[0]) - 1

                while left <= right:
                    mid2 = (left + right) // 2

                    if matrix[mid][mid2] == target:
                        return True
                    elif matrix[mid][mid2] > target:
                        right = mid2 - 1
                    else:
                        left = mid2 + 1
                return False

            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                bottom = mid - 1

        return False