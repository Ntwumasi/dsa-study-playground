"""
Longest Subarray with Sum at Most K

PATTERN: Sliding Window - Variable Size with Sum Constraint
- Find longest subarray where sum of elements <= k
- Expand window by adding elements
- Shrink when sum exceeds k

TIME COMPLEXITY: O(n) - each element added/removed at most once
SPACE COMPLEXITY: O(1) - only tracking sum and pointers

WHY THIS WORKS:
- We maintain a window with sum <= k
- When adding an element makes sum > k, we must shrink
- By removing elements from left, we decrease the sum
- This greedy approach finds the maximum valid window
"""


def find_length(nums: list[int], k: int) -> int:
    """
    Find length of longest subarray with sum at most k.

    Args:
        nums: Array of POSITIVE integers (important assumption!)
        k: Maximum allowed sum

    Returns:
        Length of longest subarray with sum <= k

    Visual:
        nums = [3, 1, 2, 7, 4, 2, 1, 1, 5], k = 8

        Window evolution:
        [3]           sum=3, valid, max=1
        [3,1]         sum=4, valid, max=2
        [3,1,2]       sum=6, valid, max=3
        [3,1,2,7]     sum=13>8, SHRINK!
        [1,2,7]       sum=10>8, SHRINK!
        [2,7]         sum=9>8, SHRINK!
        [7]           sum=7, valid, max=3
        [7,4]         sum=11>8, SHRINK!
        [4]           sum=4, valid, max=3
        [4,2]         sum=6, valid, max=3
        [4,2,1]       sum=7, valid, max=3
        [4,2,1,1]     sum=8, valid, max=4  <- NEW MAX!
        [4,2,1,1,5]   sum=13>8, SHRINK!
        ...
    """
    left = 0
    curr_sum = 0  # Current window sum
    max_length = 0

    for right in range(len(nums)):
        # Expand: add element at right to window
        curr_sum += nums[right]

        # Shrink: while sum exceeds k, remove from left
        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1

        # Update maximum (window is valid after shrinking)
        max_length = max(max_length, right - left + 1)

    return max_length


def find_length_verbose(nums: list[int], k: int) -> int:
    """
    Same algorithm with detailed comments and edge case handling.
    """
    if not nums:
        return 0

    left = 0
    curr_sum = 0
    max_length = 0

    for right in range(len(nums)):
        # Step 1: EXPAND - add nums[right] to current window
        curr_sum += nums[right]

        # Step 2: SHRINK - while window is invalid (sum > k)
        # Remove elements from left until valid again
        # NOTE: This only works for POSITIVE numbers!
        # With negatives, removing from left might increase sum
        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1

        # Step 3: UPDATE - window [left...right] is valid
        # Window size = right - left + 1
        window_size = right - left + 1
        max_length = max(max_length, window_size)

    return max_length


def find_subarray_with_sum_exactly_k(nums: list[int], k: int) -> list[int]:
    """
    Variant: Find a subarray that sums to EXACTLY k.
    Returns the subarray, or empty list if not found.
    """
    left = 0
    curr_sum = 0

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum > k and left <= right:
            curr_sum -= nums[left]
            left += 1

        if curr_sum == k:
            return nums[left:right + 1]

    return []


# Test cases
if __name__ == "__main__":
    # Longest subarray with sum <= k
    print(find_length([3, 1, 2, 7, 4, 2, 1, 1, 5], 8))  # 4
    print(find_length([1, 1, 1, 1, 1], 3))              # 3
    print(find_length([5, 5, 5], 4))                    # 0 (all elements > k)
    print(find_length([1, 2, 3], 100))                  # 3 (entire array)

    # Find exact sum
    print(find_subarray_with_sum_exactly_k([1, 2, 3, 4, 5], 9))  # [2, 3, 4]
    print(find_subarray_with_sum_exactly_k([1, 2, 3], 10))       # []

    """
    IMPORTANT ASSUMPTION:

    This algorithm assumes all numbers are POSITIVE.

    Why? Because when curr_sum > k, we shrink by removing nums[left].
    With positive numbers, this ALWAYS decreases the sum.
    With negative numbers, removing a negative could INCREASE the sum!

    For arrays with negatives, you'd need a different approach:
    - Prefix sum with hashmap
    - Or different sliding window logic
    """
