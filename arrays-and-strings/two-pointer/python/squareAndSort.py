"""
Squares of a Sorted Array (LeetCode 977)

PATTERN: Two Pointer - Opposite Direction
- Input array is sorted (but may have negatives)
- Largest squares will be at the ends (either large positive or large negative)
- Use two pointers from ends, build result from largest to smallest

TIME COMPLEXITY: O(n) - single pass through array
SPACE COMPLEXITY: O(n) - result array (O(1) if we don't count output)

WHY THIS WORKS:
- In a sorted array with negatives: [-4, -1, 0, 3, 10]
- The largest absolute values are at the ENDS
- Squares: [16, 1, 0, 9, 100] - largest are at ends!
- Compare ends, put larger square at the end of result, move that pointer
"""


def sorted_squares_optimal(nums: list[int]) -> list[int]:
    """
    Square each element and return sorted result in O(n) time.

    Args:
        nums: Sorted array of integers (may include negatives)

    Returns:
        Sorted array of squared values

    Visual:
        nums = [-4, -1, 0, 3, 10]
                L              R

        Step 1: |-4|=4 vs |10|=10 -> 10 wins, result=[_, _, _, _, 100]
        Step 2: |-4|=4 vs |3|=3   -> 4 wins,  result=[_, _, _, 16, 100]
        Step 3: |-1|=1 vs |3|=3   -> 3 wins,  result=[_, _, 9, 16, 100]
        Step 4: |-1|=1 vs |0|=0   -> 1 wins,  result=[_, 1, 9, 16, 100]
        Step 5: |0|=0             ->          result=[0, 1, 9, 16, 100]
    """
    n = len(nums)
    result = [0] * n  # Pre-allocate result array

    left = 0
    right = n - 1
    position = n - 1  # Fill result from the end (largest first)

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            # Left has larger absolute value
            result[position] = left_square
            left += 1
        else:
            # Right has larger or equal absolute value
            result[position] = right_square
            right -= 1

        position -= 1

    return result


def sorted_squares_naive(nums: list[int]) -> list[int]:
    """
    Naive approach: square all elements then sort.

    TIME: O(n log n) due to sorting
    SPACE: O(n) for the result

    This is simpler but less optimal than the two-pointer approach.
    """
    return sorted(num ** 2 for num in nums)


# Test cases
if __name__ == "__main__":
    # Optimal O(n) solution
    print(sorted_squares_optimal([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
    print(sorted_squares_optimal([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]
    print(sorted_squares_optimal([1, 2, 3, 4, 5]))     # [1, 4, 9, 16, 25]
    print(sorted_squares_optimal([-5, -4, -3, -2]))    # [4, 9, 16, 25]

    # Verify naive solution gives same result
    print(sorted_squares_naive([-4, -1, 0, 3, 10]))    # [0, 1, 9, 16, 100]
