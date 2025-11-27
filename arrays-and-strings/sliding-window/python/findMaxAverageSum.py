"""
Maximum Average Subarray (Alternative Implementation)

PATTERN: Sliding Window - Fixed Size
- Same problem as findMaxAverage.py
- Different implementation style with named variables

TIME COMPLEXITY: O(n) - single pass through array
SPACE COMPLEXITY: O(1) - only tracking sums

This file demonstrates the "outgoing/incoming" mental model
for understanding sliding windows.
"""


def find_max_average_sum(nums: list[int], k: int) -> float:
    """
    Find maximum average of any k-length contiguous subarray.

    Args:
        nums: Array of integers
        k: Window size

    Returns:
        Maximum average value

    Visual - The Sliding Concept:
        nums = [1, 2, 3, 4, 5], k = 3

        Initial window:
        [1, 2, 3] 4, 5
         └─────┘
         sum = 6

        Slide 1:
         1 [2, 3, 4] 5
            └─────┘
         outgoing = 1 (leaves)
         incoming = 4 (enters)
         sum = 6 - 1 + 4 = 9

        Slide 2:
         1, 2 [3, 4, 5]
              └─────┘
         outgoing = 2
         incoming = 5
         sum = 9 - 2 + 5 = 12
    """
    # Initialize window with first k elements
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide window from position k to end
    for i in range(k, len(nums)):
        # Identify elements crossing window boundary
        outgoing = nums[i - k]  # Left element leaving window
        incoming = nums[i]       # Right element entering window

        # Update sum in O(1) instead of recalculating
        window_sum = window_sum - outgoing + incoming

        # Track the maximum sum seen
        max_sum = max(window_sum, max_sum)

    # Calculate and return average
    return max_sum / k


def find_max_sum_subarray(nums: list[int], k: int) -> int:
    """
    Variant: Return the maximum SUM (not average) of k elements.

    Sometimes you just need the sum, not the average.
    """
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


# Test cases
if __name__ == "__main__":
    # Maximum average
    print(find_max_average_sum([1, 12, -5, -6, 50, 3], 4))  # 12.75
    print(find_max_average_sum([1, 2, 3, 4, 5], 3))          # 4.0

    # Maximum sum
    print(find_max_sum_subarray([1, 2, 3, 4, 5], 3))  # 12 (3+4+5)
    print(find_max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # 9 (5+1+3)

    """
    KEY MENTAL MODEL:

    Think of the window as a physical window sliding over data:

    Data:    [a] [b] [c] [d] [e] [f]
              ├───────────┤
              Window of size 4

    When we slide:
    - 'a' exits through the left (outgoing)
    - 'e' enters through the right (incoming)

    Window state = Old state - outgoing + incoming

    This "subtract and add" pattern is the core of sliding window!
    """
