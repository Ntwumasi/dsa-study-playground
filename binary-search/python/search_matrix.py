"""
Search a 2D Matrix (LeetCode 74)

PATTERN: Binary Search on Virtual 1D Array
- Treat 2D matrix as a flattened 1D sorted array
- Use binary search with index conversion

TIME COMPLEXITY: O(log(m*n)) - binary search on m*n elements
SPACE COMPLEXITY: O(1) - only using pointers

WHY THIS WORKS:
- Matrix has these properties:
  1. Each row is sorted left to right
  2. First element of each row > last element of previous row
- This means entire matrix is sorted when read row by row!
- We can binary search on a "virtual" 1D array

KEY INSIGHT:
- For a flattened index 'mid' in a matrix with n columns:
  - row = mid // n (integer division)
  - col = mid % n  (remainder)
"""


class Solution:
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Search for target in a sorted 2D matrix.

        Args:
            matrix: m x n sorted matrix
            target: Value to find

        Returns:
            True if found, False otherwise

        Visual:
            matrix = [
                [1,  3,  5,  7],    indices 0-3
                [10, 11, 16, 20],   indices 4-7
                [23, 30, 34, 60]    indices 8-11
            ]
            target = 3

            Treat as 1D: [1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]

            mid = 5 → row = 5//4 = 1, col = 5%4 = 1 → matrix[1][1] = 11
            11 > 3 → search left

            mid = 2 → row = 2//4 = 0, col = 2%4 = 2 → matrix[0][2] = 5
            5 > 3 → search left

            mid = 0 → row = 0//4 = 0, col = 0%4 = 0 → matrix[0][0] = 1
            1 < 3 → search right

            mid = 1 → row = 1//4 = 0, col = 1%4 = 1 → matrix[0][1] = 3
            3 == target ✓ FOUND!
        """
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)      # Number of rows
        n = len(matrix[0])   # Number of columns

        # Binary search on virtual 1D array of size m*n
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            # Convert 1D index to 2D coordinates
            row = mid // n  # Which row?
            col = mid % n   # Which column?

            num = matrix[row][col]

            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


def search_matrix_two_searches(matrix: list[list[int]], target: int) -> bool:
    """
    Alternative: Two binary searches.

    1. Binary search to find the correct row
    2. Binary search within that row

    Same time complexity, but more intuitive for some.
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])

    # Find the row where target could be
    top, bottom = 0, m - 1
    while top <= bottom:
        mid_row = (top + bottom) // 2
        if target > matrix[mid_row][-1]:
            # Target larger than row's max, search below
            top = mid_row + 1
        elif target < matrix[mid_row][0]:
            # Target smaller than row's min, search above
            bottom = mid_row - 1
        else:
            # Target is in this row
            break

    if top > bottom:
        return False

    # Binary search within the row
    row = (top + bottom) // 2
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Test cases
if __name__ == "__main__":
    sol = Solution()

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]

    # Found cases
    print(sol.search_matrix(matrix, 3))   # True
    print(sol.search_matrix(matrix, 11))  # True
    print(sol.search_matrix(matrix, 60))  # True

    # Not found cases
    print(sol.search_matrix(matrix, 13))  # False
    print(sol.search_matrix(matrix, 0))   # False
    print(sol.search_matrix(matrix, 100)) # False

    # Edge cases
    print(sol.search_matrix([[1]], 1))    # True
    print(sol.search_matrix([[1]], 2))    # False

    """
    INDEX CONVERSION FORMULA:

    For matrix with n columns:
    - 1D index → 2D: row = idx // n, col = idx % n
    - 2D → 1D index: idx = row * n + col

    Example (n=4):
    idx=0  → (0,0)    idx=4  → (1,0)    idx=8  → (2,0)
    idx=1  → (0,1)    idx=5  → (1,1)    idx=9  → (2,1)
    idx=2  → (0,2)    idx=6  → (1,2)    idx=10 → (2,2)
    idx=3  → (0,3)    idx=7  → (1,3)    idx=11 → (2,3)
    """
