"""
Prefix Sum Template

PATTERN: Prefix Sum (Cumulative Sum)
- Build an array where each element is the sum of all elements up to that index
- Enables O(1) range sum queries after O(n) preprocessing

TIME COMPLEXITY:
- Build prefix array: O(n)
- Query any range sum: O(1)

SPACE COMPLEXITY: O(n) for the prefix array

WHEN TO USE:
- Multiple range sum queries on a static array
- Finding subarrays with specific sum properties
- Problems involving cumulative totals

KEY FORMULA:
- sum(arr[i..j]) = prefix[j] - prefix[i-1]
- Or with 0-indexed prefix: sum(arr[i..j]) = prefix[j+1] - prefix[i]
"""


def build_prefix_sum(arr: list[int]) -> list[int]:
    """
    Build a prefix sum array from input array.

    Args:
        arr: Input array of numbers

    Returns:
        Prefix sum array where prefix[i] = sum(arr[0..i])

    Visual:
        arr    = [2, 3, 5, 1, 6]
        prefix = [2, 5, 10, 11, 17]

        How it's built:
        prefix[0] = 2                    (just arr[0])
        prefix[1] = 2 + 3 = 5            (prefix[0] + arr[1])
        prefix[2] = 5 + 5 = 10           (prefix[1] + arr[2])
        prefix[3] = 10 + 1 = 11          (prefix[2] + arr[3])
        prefix[4] = 11 + 6 = 17          (prefix[3] + arr[4])
    """
    if not arr:
        return []

    # Start with first element
    prefix = [arr[0]]

    # Build rest of prefix sum
    for i in range(1, len(arr)):
        # Each prefix[i] = prefix[i-1] + arr[i]
        prefix.append(prefix[-1] + arr[i])

    return prefix


def build_prefix_sum_with_zero(arr: list[int]) -> list[int]:
    """
    Alternative: Prefix sum array with leading zero.

    This makes range queries cleaner:
    sum(arr[i..j]) = prefix[j+1] - prefix[i]

    Visual:
        arr    = [2, 3, 5, 1, 6]
        prefix = [0, 2, 5, 10, 11, 17]
                  ^-- leading zero

        sum(arr[1..3]) = prefix[4] - prefix[1] = 11 - 2 = 9
        Verify: arr[1] + arr[2] + arr[3] = 3 + 5 + 1 = 9 ✓
    """
    prefix = [0]  # Start with zero
    for num in arr:
        prefix.append(prefix[-1] + num)
    return prefix


def range_sum(prefix: list[int], left: int, right: int) -> int:
    """
    Get sum of elements from index left to right (inclusive).

    Assumes prefix was built WITH leading zero.

    Args:
        prefix: Prefix sum array with leading zero
        left: Start index (0-based)
        right: End index (0-based, inclusive)

    Returns:
        Sum of arr[left..right]
    """
    return prefix[right + 1] - prefix[left]


# Test cases
if __name__ == "__main__":
    arr = [2, 3, 5, 1, 6]

    # Standard prefix sum
    prefix = build_prefix_sum(arr)
    print(f"Array:  {arr}")
    print(f"Prefix: {prefix}")  # [2, 5, 10, 11, 17]

    # Prefix sum with leading zero (more convenient for queries)
    prefix_zero = build_prefix_sum_with_zero(arr)
    print(f"Prefix (with zero): {prefix_zero}")  # [0, 2, 5, 10, 11, 17]

    # Range sum queries
    print(f"Sum of arr[1..3]: {range_sum(prefix_zero, 1, 3)}")  # 9 (3+5+1)
    print(f"Sum of arr[0..4]: {range_sum(prefix_zero, 0, 4)}")  # 17 (entire array)
    print(f"Sum of arr[2..2]: {range_sum(prefix_zero, 2, 2)}")  # 5 (single element)

    """
    WHY PREFIX SUM IS POWERFUL:

    Without prefix sum:
    - Each range query requires O(n) time to sum elements
    - k queries = O(k * n) total

    With prefix sum:
    - O(n) preprocessing to build prefix array
    - O(1) per query using formula: sum[i..j] = prefix[j+1] - prefix[i]
    - k queries = O(n + k) total

    When k is large, prefix sum wins significantly!
    """
