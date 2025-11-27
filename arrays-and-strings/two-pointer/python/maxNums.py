"""
Find Maximum in Array

PATTERN: Linear Scan (Not actually Two Pointer!)
- This is a simple iteration pattern, not two pointers
- Track the maximum value seen so far as we scan

TIME COMPLEXITY: O(n) - must check every element
SPACE COMPLEXITY: O(1) - only storing max value

NOTE: This problem doesn't use two pointers. It's included here
for completeness but should perhaps be moved to a "basics" folder.
Python's built-in max() does this more efficiently.
"""


def find_max(nums: list[int]) -> int:
    """
    Find the maximum number in a list.

    Args:
        nums: Non-empty list of numbers

    Returns:
        Maximum value in the list

    Raises:
        IndexError: If nums is empty

    Visual:
        nums = [3, 1, 4, 1, 5, 9, 2, 6]

        max_num = 3 (start with first element)
        3 vs 1 → max stays 3
        3 vs 4 → max becomes 4
        4 vs 1 → max stays 4
        4 vs 5 → max becomes 5
        5 vs 9 → max becomes 9
        9 vs 2 → max stays 9
        9 vs 6 → max stays 9

        Return 9
    """
    if not nums:
        raise IndexError("Cannot find max of empty list")

    max_num = nums[0]

    for num in nums:
        if num > max_num:
            max_num = num

    return max_num


def find_max_with_index(nums: list[int]) -> tuple[int, int]:
    """
    Find max value AND its index.

    Args:
        nums: Non-empty list of numbers

    Returns:
        Tuple of (max_value, index)
    """
    if not nums:
        raise IndexError("Cannot find max of empty list")

    max_num = nums[0]
    max_index = 0

    for i, num in enumerate(nums):
        if num > max_num:
            max_num = num
            max_index = i

    return max_num, max_index


def find_min_max(nums: list[int]) -> tuple[int, int]:
    """
    Find both min and max in a single pass.

    Args:
        nums: Non-empty list of numbers

    Returns:
        Tuple of (min_value, max_value)
    """
    if not nums:
        raise IndexError("Cannot find min/max of empty list")

    min_num = max_num = nums[0]

    for num in nums:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    return min_num, max_num


# Test cases
if __name__ == "__main__":
    # Basic max
    print(find_max([1, 2, 3, 4, 5]))        # 5
    print(find_max([5, 4, 3, 2, 1]))        # 5
    print(find_max([-1, -5, -2]))           # -1
    print(find_max([42]))                   # 42

    # Max with index
    print(find_max_with_index([3, 1, 4, 1, 5, 9]))  # (9, 5)

    # Min and max together
    print(find_min_max([3, 1, 4, 1, 5, 9, 2, 6]))   # (1, 9)

    # Pythonic alternative (recommended in practice)
    print(max([1, 2, 3, 4, 5]))  # 5 - use built-in!
