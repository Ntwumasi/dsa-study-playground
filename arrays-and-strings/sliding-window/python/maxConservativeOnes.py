"""
Max Consecutive Ones III (LeetCode 1004)

PATTERN: Sliding Window - Variable Size with Constraint
- Find longest subarray of 1s, allowing at most k flips of 0s to 1s
- Window is valid as long as it contains at most k zeros
- Expand right, shrink left when zeros exceed k

TIME COMPLEXITY: O(n) - each element visited at most twice
SPACE COMPLEXITY: O(1) - only tracking counts

WHY THIS WORKS:
- We're essentially finding the longest window containing at most k zeros
- Flipping a 0 to 1 is equivalent to "tolerating" that 0 in our window
- When we have more than k zeros, we must shrink to maintain validity
"""


def longest_ones(nums: list[int], k: int) -> int:
    """
    Find longest contiguous subarray of 1s after flipping at most k 0s.

    Args:
        nums: Binary array (contains only 0s and 1s)
        k: Maximum number of 0s we can flip to 1s

    Returns:
        Length of longest subarray of all 1s achievable

    Visual:
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2

        We can flip at most 2 zeros to ones.

        Window grows:
        [1, 1, 1, 0, 0] -> 2 zeros, valid (k=2)
        [1, 1, 1, 0, 0, 0] -> 3 zeros, INVALID! shrink left
        [1, 1, 0, 0, 0] -> still 3 zeros, shrink more
        [1, 0, 0, 0] -> still 3 zeros, shrink more
        [0, 0, 0] -> still 3 zeros, shrink more
        [0, 0] -> 2 zeros, valid again, continue expanding

        Best window: [0, 0, 1, 1, 1, 1] with 2 flips -> length 6
    """
    left = 0
    max_length = 0
    zero_count = 0  # Number of zeros in current window

    for right in range(len(nums)):
        # Expand: add element at right to window
        if nums[right] == 0:
            zero_count += 1

        # Shrink: while we have too many zeros, remove from left
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Update maximum (current window is always valid here)
        max_length = max(max_length, right - left + 1)

    return max_length


def longest_ones_alternative(nums: list[int], k: int) -> int:
    """
    Alternative approach: track ones instead of zeros.

    The insight: in a valid window of size w with z zeros,
    we have (w - z) ones. If z <= k, window is valid.
    """
    left = 0
    max_length = 0

    for right in range(len(nums)):
        # If current element is 0, use one of our k flips
        if nums[right] == 0:
            k -= 1

        # If we've used more than allowed flips, shrink
        while k < 0:
            if nums[left] == 0:
                k += 1  # Recover a flip as we remove a 0
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


# Test cases
if __name__ == "__main__":
    # Example 1
    print(longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))  # 6
    # Flip zeros at index 5 and 10: [1,1,1,0,0,1,1,1,1,1,1]
    # Longest consecutive 1s: indices 5-10, length 6

    # Example 2
    print(longest_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
    # 10

    # Edge cases
    print(longest_ones([1, 1, 1, 1], 0))  # 4 (no flips needed)
    print(longest_ones([0, 0, 0, 0], 4))  # 4 (flip all zeros)
    print(longest_ones([0, 0, 0, 0], 2))  # 2 (can only flip 2)

    """
    PATTERN RECOGNITION:

    This is a classic "find longest subarray satisfying constraint" problem.
    The constraint is: at most k zeros in the window.

    Similar problems:
    - Longest subarray with sum <= k
    - Longest substring with at most k distinct characters
    - Minimum window substring

    The sliding window template applies:
    1. Expand right (add element)
    2. While constraint broken, shrink left
    3. Update answer with valid window
    """
