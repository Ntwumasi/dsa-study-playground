"""
Sliding Window Template

PATTERN: Sliding Window (Variable Size)
- Maintain a "window" of elements that satisfies some condition
- Expand window by moving right pointer
- Shrink window by moving left pointer when condition breaks
- Track the answer (usually max/min window size)

TWO TYPES OF SLIDING WINDOW:
1. Fixed-size window: Window always has size k
2. Variable-size window: Window grows/shrinks based on condition

TIME COMPLEXITY: O(n) - each element is visited at most twice
SPACE COMPLEXITY: O(1) or O(k) depending on what we track

WHEN TO USE:
- Finding subarrays/substrings that satisfy some condition
- Problems asking for "contiguous" sequences
- Optimization problems on subarrays (max/min length, sum, etc.)
"""


def sliding_window_variable_template(arr: list) -> int:
    """
    Template for VARIABLE-size sliding window.

    Use when: window size changes based on a condition
    Examples: longest substring without repeating chars, max sum <= k

    Visual:
        arr = [a, b, c, d, e, f]
               L        R          <- window is [a, b, c, d]

        If condition breaks:
               arr = [a, b, c, d, e, f]
                         L     R       <- shrink by moving L right
    """
    left = 0
    ans = 0
    curr = 0  # Current window state (sum, count, etc.)

    for right in range(len(arr)):
        # Step 1: Expand window - add arr[right] to current state
        curr += arr[right]  # Example: add to sum

        # Step 2: Shrink window while condition is broken
        while curr > 10:  # Example condition: sum exceeds threshold
            curr -= arr[left]  # Remove left element from state
            left += 1

        # Step 3: Update answer with current valid window
        ans = max(ans, right - left + 1)

    return ans


def sliding_window_fixed_template(arr: list, k: int) -> int:
    """
    Template for FIXED-size sliding window.

    Use when: window must always have exactly k elements
    Examples: max average of k elements, max sum of k elements

    Visual:
        k = 3
        arr = [1, 2, 3, 4, 5]
              [-----]           <- initial window sum = 6
                 [-----]        <- slide: remove 1, add 4, sum = 9
                    [-----]     <- slide: remove 2, add 5, sum = 12
    """
    # Initialize first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(arr)):
        # Remove element leaving window, add element entering
        outgoing = arr[i - k]
        incoming = arr[i]
        window_sum = window_sum - outgoing + incoming

        max_sum = max(max_sum, window_sum)

    return max_sum


def sliding_window_with_hashmap_template(s: str) -> int:
    """
    Template for sliding window with character frequency tracking.

    Use when: need to track counts of elements in window
    Examples: longest substring with at most k distinct chars
    """
    from collections import defaultdict

    left = 0
    ans = 0
    char_count = defaultdict(int)

    for right in range(len(s)):
        # Add right character to window
        char_count[s[right]] += 1

        # Shrink window while condition is broken
        while len(char_count) > 2:  # Example: more than 2 distinct chars
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        # Update answer
        ans = max(ans, right - left + 1)

    return ans


"""
KEY INSIGHT:
The "sliding" part means we're efficiently reusing previous computation.
Instead of recalculating the entire window each time, we just:
- Add the new element entering the window
- Remove the old element leaving the window

This transforms O(n*k) brute force into O(n) sliding window!
"""
