"""
Subarray Sum Queries with Prefix Sum

PATTERN: Prefix Sum for Range Queries
- Build prefix sum array once: O(n)
- Answer multiple range sum queries: O(1) each

TIME COMPLEXITY:
- Preprocessing: O(n)
- Per query: O(1)
- Total for m queries: O(n + m)

SPACE COMPLEXITY: O(n) for prefix array

WHY THIS WORKS:
- prefix[i] = sum of all elements from index 0 to i
- sum(arr[x..y]) = prefix[y] - prefix[x-1]
- With leading zero: sum(arr[x..y]) = prefix[y+1] - prefix[x]
"""


def answer_queries(nums: list[int], queries: list[list[int]], limit: int) -> list[bool]:
    """
    For each query [x, y], check if sum(nums[x..y]) < limit.

    Args:
        nums: Array of integers
        queries: List of [start, end] index pairs
        limit: Threshold to compare against

    Returns:
        List of booleans - True if subarray sum < limit

    Visual:
        nums = [1, 6, 3, 2, 7, 2]
        queries = [[0, 3], [2, 5], [2, 4]]
        limit = 13

        Build prefix (with leading zero for cleaner formula):
        prefix = [0, 1, 7, 10, 12, 19, 21]

        Query [0, 3]: sum = prefix[4] - prefix[0] = 12 - 0 = 12 < 13? True
        Query [2, 5]: sum = prefix[6] - prefix[2] = 21 - 7 = 14 < 13? False
        Query [2, 4]: sum = prefix[5] - prefix[2] = 19 - 7 = 12 < 13? True

        Result: [True, False, True]
    """
    # Build prefix sum with leading zero
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)

    # Answer each query in O(1)
    results = []
    for x, y in queries:
        # Sum of nums[x..y] = prefix[y+1] - prefix[x]
        subarray_sum = prefix[y + 1] - prefix[x]
        results.append(subarray_sum < limit)

    return results


def answer_queries_alternative(nums: list[int], queries: list[list[int]], limit: int) -> list[bool]:
    """
    Alternative implementation with prefix starting from first element.

    This requires slightly different formula for range sum.
    """
    if not nums:
        return [False] * len(queries)

    # Build prefix without leading zero
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    results = []
    for x, y in queries:
        # sum(nums[x..y]) = prefix[y] - prefix[x-1] (if x > 0)
        # sum(nums[0..y]) = prefix[y] (if x == 0)
        if x == 0:
            subarray_sum = prefix[y]
        else:
            subarray_sum = prefix[y] - prefix[x - 1]

        results.append(subarray_sum < limit)

    return results


# Test cases
if __name__ == "__main__":
    nums = [1, 6, 3, 2, 7, 2]
    queries = [[0, 3], [2, 5], [2, 4]]
    limit = 13

    print(answer_queries(nums, queries, limit))  # [True, False, True]

    # Verify manually:
    # sum(nums[0:4]) = 1+6+3+2 = 12 < 13 ✓
    # sum(nums[2:6]) = 3+2+7+2 = 14 < 13 ✗
    # sum(nums[2:5]) = 3+2+7 = 12 < 13 ✓

    # Test alternative implementation
    print(answer_queries_alternative(nums, queries, limit))  # [True, False, True]

    """
    COMPLEXITY COMPARISON:

    Naive approach (no prefix sum):
    - Each query: O(n) to sum the range
    - m queries: O(m * n)

    With prefix sum:
    - Build prefix: O(n)
    - Each query: O(1)
    - m queries: O(n + m)

    When m >> 1, prefix sum is significantly faster!
    Example: n=1000, m=10000
    - Naive: 10,000,000 operations
    - Prefix: 11,000 operations (900x faster!)
    """
