"""
Search a 2D Matrix - Alternative Implementation

PATTERN: Binary Search on Flattened Matrix
- Same concept as search_matrix.py
- This file provides an alternative perspective

TIME COMPLEXITY: O(log(m*n))
SPACE COMPLEXITY: O(1)

This is the same algorithm as search_matrix.py but with slightly
different code organization. Keeping both for reference.
"""


def find_in_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Search for target in a sorted 2D matrix using binary search.

    The matrix has the property that:
    1. Integers in each row are sorted from left to right
    2. First integer of each row is greater than last integer of previous row

    Args:
        matrix: Sorted 2D matrix
        target: Value to search for

    Returns:
        True if target exists in matrix, False otherwise

    Visual Concept:
        Think of the 2D matrix as a 1D sorted array:

        Matrix:              Flattened:
        [1,  3,  5,  7]     [1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 50]
        [10, 11, 16, 20]     0  1  2  3   4   5   6   7   8   9  10  11
        [23, 30, 34, 50]

        To convert index 'i' to matrix coordinates:
        - row = i // num_columns
        - col = i % num_columns

        Example: index 7 in matrix with 4 columns
        - row = 7 // 4 = 1
        - col = 7 % 4 = 3
        - matrix[1][3] = 20 ✓
    """
    # Handle edge cases
    if not matrix or not matrix[0]:
        return False

    m = len(matrix)      # Number of rows
    n = len(matrix[0])   # Number of columns
    total_elements = m * n

    # Binary search on the "virtual" 1D array
    left = 0
    right = total_elements - 1

    while left <= right:
        mid = (left + right) // 2

        # Convert 1D index to 2D matrix coordinates
        row = mid // n
        col = mid % n
        value = matrix[row][col]

        if value == target:
            return True
        elif value > target:
            # Target is smaller, search left half
            right = mid - 1
        else:
            # Target is larger, search right half
            left = mid + 1

    return False


def find_in_matrix_with_position(matrix: list[list[int]], target: int) -> tuple[int, int] | None:
    """
    Same as above but returns the (row, col) position if found.
    """
    if not matrix or not matrix[0]:
        return None

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row, col = mid // n, mid % n
        value = matrix[row][col]

        if value == target:
            return (row, col)
        elif value > target:
            right = mid - 1
        else:
            left = mid + 1

    return None


# Test cases
if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]

    # Boolean search
    print(find_in_matrix(matrix, 3))   # True
    print(find_in_matrix(matrix, 13))  # False

    # Position search
    print(find_in_matrix_with_position(matrix, 16))  # (1, 2)
    print(find_in_matrix_with_position(matrix, 13))  # None

    # Complexity demonstration
    print("\nComplexity Analysis:")
    print(f"Matrix size: {len(matrix)} x {len(matrix[0])} = {len(matrix) * len(matrix[0])} elements")
    print(f"Max comparisons with binary search: ~{(len(matrix) * len(matrix[0])).bit_length()} (log₂)")
    print(f"Max comparisons with linear search: {len(matrix) * len(matrix[0])}")

    """
    RELATED PROBLEMS:

    1. Search a 2D Matrix (LeetCode 74) - This problem
       - Matrix is fully sorted (row by row)
       - Single binary search works

    2. Search a 2D Matrix II (LeetCode 240)
       - Each row is sorted, each column is sorted
       - But first of next row NOT necessarily > last of current row
       - Requires different approach (start from top-right or bottom-left)
    """
