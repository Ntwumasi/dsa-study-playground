"""
Binary Search Template

PATTERN: Binary Search - Divide and Conquer
- Repeatedly divide search space in half
- Works on SORTED arrays/data
- Eliminates half the remaining elements each iteration

TIME COMPLEXITY: O(log n) - halve the search space each step
SPACE COMPLEXITY: O(1) for iterative, O(log n) for recursive

WHEN TO USE:
- Searching in sorted arrays
- Finding boundaries (first/last occurrence)
- Optimization problems with monotonic condition
- Any problem where you can eliminate half the search space

KEY INSIGHT:
- If searching for target in sorted array:
  - If mid < target, answer must be in right half
  - If mid > target, answer must be in left half
"""


def binary_search_basic(nums: list[int], target: int) -> int:
    """
    Standard binary search to find target in sorted array.

    Args:
        nums: Sorted array of integers
        target: Value to find

    Returns:
        Index of target, or -1 if not found

    Visual:
        nums = [1, 3, 5, 7, 9, 11, 13], target = 7

        Step 1: left=0, right=6, mid=3
                nums[3]=7 == target  FOUND!

        Another example: target = 5
        Step 1: left=0, right=6, mid=3, nums[3]=7 > 5 ’ go left
        Step 2: left=0, right=2, mid=1, nums[1]=3 < 5 ’ go right
        Step 3: left=2, right=2, mid=2, nums[2]=5 == target  FOUND!
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        # Calculate mid (avoid integer overflow in other languages)
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # Target is in right half
            left = mid + 1
        else:
            # Target is in left half
            right = mid - 1

    return -1  # Target not found


def binary_search_left_bound(nums: list[int], target: int) -> int:
    """
    Find the LEFTMOST (first) occurrence of target.

    Returns: Index of first occurrence, or insertion point if not found.

    Use case: "Find first element >= target"
    """
    left = 0
    right = len(nums)  # Note: right = len, not len-1

    while left < right:  # Note: < not <=
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid  # Don't skip mid, it might be the answer

    return left  # Position where target should be


def binary_search_right_bound(nums: list[int], target: int) -> int:
    """
    Find the RIGHTMOST (last) occurrence of target.

    Returns: Index of last occurrence + 1, or insertion point if not found.

    Use case: "Find first element > target"
    """
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] <= target:  # Note: <= not <
            left = mid + 1
        else:
            right = mid

    return left  # Position after last occurrence


def binary_search_recursive(nums: list[int], target: int, left: int, right: int) -> int:
    """
    Recursive implementation of binary search.

    Generally prefer iterative for better space efficiency.
    """
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


# Test cases
if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11, 13]

    # Basic search
    print(binary_search_basic(nums, 7))   # 3
    print(binary_search_basic(nums, 4))   # -1 (not found)

    # With duplicates
    dups = [1, 2, 2, 2, 3, 4]
    print(binary_search_left_bound(dups, 2))   # 1 (first 2)
    print(binary_search_right_bound(dups, 2))  # 4 (position after last 2)

    # Recursive
    print(binary_search_recursive(nums, 9, 0, len(nums) - 1))  # 4

    """
    COMMON BINARY SEARCH VARIATIONS:

    1. Find exact match:
       - Standard template with left <= right
       - Return mid when found

    2. Find first occurrence (left bound):
       - Continue searching left even after finding target
       - right = mid (don't skip mid)

    3. Find last occurrence (right bound):
       - Continue searching right even after finding target
       - left = mid + 1

    4. Find insertion position:
       - Same as left bound
       - Returns where element should be inserted

    5. Search for condition:
       - Instead of comparing with target
       - Check if condition is satisfied at mid
       - Find first/last position where condition holds
    """
