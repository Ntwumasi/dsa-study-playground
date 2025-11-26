def find_mid_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False  # Edge case: empty matrix

    m = len(matrix)       # number of rows
    n = len(matrix[0])    # number of columns

    left = 0
    right = m * n - 1     # Treat 2D matrix as a flattened 1D array

    while left <= right:
        mid = (left + right) // 2
        row = mid // n    # Get row index
        col = mid % n     # Get column index
        num = matrix[row][col]

        if num == target:
            return True
        elif num > target:
            right = mid - 1
        else:
            left = mid + 1

    return False  # Target not found
