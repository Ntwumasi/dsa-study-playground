"""
Maximum Average Subarray I (LeetCode 643)

PATTERN: Sliding Window - Fixed Size
- Window must be exactly k elements
- Slide window across array, track maximum sum
- Return max sum divided by k

TIME COMPLEXITY: O(n) - single pass through array
SPACE COMPLEXITY: O(1) - only tracking current and max sum

WHY THIS WORKS:
- Instead of recalculating sum for each window (O(n*k))
- We "slide" by removing outgoing element and adding incoming (O(1) per slide)
- Total: O(n) instead of O(n*k)
"""


def find_max_average(nums: list[int], k: int) -> float:
    """
    Find contiguous subarray of length k with maximum average.

    Args:
        nums: Array of integers
        k: Required window size

    Returns:
        Maximum average value of any k-length subarray

    Visual:
        nums = [1, 12, -5, -6, 50, 3], k = 4

        Window 1: [1, 12, -5, -6] = 2      (sum=2)
        Window 2: [12, -5, -6, 50] = 51    (sum=51) <- MAX
        Window 3: [-5, -6, 50, 3] = 42     (sum=42)

        Return 51/4 = 12.75
    """
    # Initialize: calculate sum of first window
    curr_sum = sum(nums[:k])
    max_sum = curr_sum

    # Slide window across the rest of the array
    for i in range(k, len(nums)):
        # Slide: remove element leaving (i-k), add element entering (i)
        #
        # Before: [..., nums[i-k], ..., nums[i-1]]  <- old window
        # After:  [..., nums[i-k+1], ..., nums[i]]  <- new window
        #
        curr_sum += nums[i] - nums[i - k]

        # Update maximum
        max_sum = max(max_sum, curr_sum)

    # Return average
    return max_sum / k


def find_max_average_verbose(nums: list[int], k: int) -> float:
    """
    Same algorithm with more explicit variable names.
    """
    # Calculate initial window sum
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        outgoing = nums[i - k]  # Element leaving the window
        incoming = nums[i]       # Element entering the window

        # Update window sum by sliding
        window_sum = window_sum - outgoing + incoming

        # Track maximum
        max_sum = max(max_sum, window_sum)

    return max_sum / k


# Test cases
if __name__ == "__main__":
    print(find_max_average([1, 12, -5, -6, 50, 3], 4))  # 12.75
    print(find_max_average([5], 1))                      # 5.0
    print(find_max_average([0, 1, 1, 3, 3], 4))         # 2.0
    print(find_max_average([-1], 1))                     # -1.0

    """
    COMPLEXITY BREAKDOWN:

    Brute Force: O(n * k)
    - For each starting position, sum k elements
    - n starting positions × k elements = O(n*k)

    Sliding Window: O(n)
    - Initial sum: O(k)
    - Sliding: O(n-k) operations, each O(1)
    - Total: O(k) + O(n-k) = O(n)

    Space: O(1) - only storing two numbers
    """
