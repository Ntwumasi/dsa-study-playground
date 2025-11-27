"""
Two Sum II - Input Array Is Sorted (LeetCode 167)

PATTERN: Two Pointer - Opposite Direction
- Use two pointers starting at opposite ends of a SORTED array
- Move pointers inward based on comparison with target

TIME COMPLEXITY: O(n) - each element visited at most once
SPACE COMPLEXITY: O(1) - only using two pointers

WHY THIS WORKS:
- Since array is sorted, if sum is too small, move left pointer right (increase sum)
- If sum is too large, move right pointer left (decrease sum)
- This guarantees we find the pair if it exists
"""


def two_sum_sorted(nums: list[int], target: int) -> list[int] | None:
    """
    Find two numbers in a SORTED array that add up to target.

    Args:
        nums: Sorted array of integers
        target: Target sum to find

    Returns:
        1-indexed positions of the two numbers, or None if not found
    """
    # Initialize pointers at opposite ends
    left = 0
    right = len(nums) - 1

    # Continue until pointers meet
    while left < right:
        # Calculate current sum
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            # Found the pair! Return 1-indexed positions
            return [left + 1, right + 1]
        elif current_sum < target:
            # Sum too small - need larger numbers, move left pointer right
            left += 1
        else:
            # Sum too large - need smaller numbers, move right pointer left
            right -= 1

    # No valid pair found
    return None


# Test cases
if __name__ == "__main__":
    print(two_sum_sorted([2, 7, 11, 15], 9))   # [1, 2] -> 2 + 7 = 9
    print(two_sum_sorted([2, 3, 4], 6))        # [1, 3] -> 2 + 4 = 6
    print(two_sum_sorted([-1, 0, 1, 2], 1))    # [2, 4] -> 0 + 1 = 1 (wait, that's wrong)
    print(two_sum_sorted([-1, 0], 5))          # None - no valid pair
