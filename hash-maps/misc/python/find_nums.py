"""
Find Lonely Numbers

PATTERN: Hash Set - Neighbor Existence Check
- Convert array to set for O(1) lookups
- Check if neighbors (x-1, x+1) exist for each number

TIME COMPLEXITY: O(n) - convert to set + single pass
SPACE COMPLEXITY: O(n) - set storage

WHY THIS WORKS:
- A number is "lonely" if neither x-1 nor x+1 exists in the array
- Set provides O(1) lookup for neighbor checks
- Much faster than O(n) linear search for each check
"""


def find_numbers(nums: list[int]) -> list[int]:
    """
    Find all unique numbers x where x+1 and x-1 are NOT in nums.

    Args:
        nums: Integer array

    Returns:
        List of lonely numbers (no adjacent values exist)

    Visual:
        nums = [10, 6, 5, 8]

        Convert to set: {10, 6, 5, 8}

        Check each number:
        - 10: 9 in set? No, 11 in set? No -> lonely! ✓
        - 6:  5 in set? Yes -> not lonely
        - 5:  4 in set? No, 6 in set? Yes -> not lonely
        - 8:  7 in set? No, 9 in set? No -> lonely! ✓

        Answer: [10, 8]

    Another example:
        nums = [1, 3, 5, 7]
        All numbers are lonely (no consecutive values)
        Answer: [1, 3, 5, 7]
    """
    ans = []
    nums_set = set(nums)  # O(1) lookups

    for num in nums_set:
        # Check if neither neighbor exists
        if (num + 1 not in nums_set) and (num - 1 not in nums_set):
            ans.append(num)

    return ans


def find_lonely_with_frequency(nums: list[int]) -> list[int]:
    """
    Alternative: Also require number appears exactly once.

    This is LeetCode 2150 - Find All Lonely Numbers in the Array.
    A number is lonely if it appears exactly once AND has no adjacent values.
    """
    from collections import Counter

    freq = Counter(nums)
    result = []

    for num, count in freq.items():
        # Must appear exactly once AND no neighbors
        if count == 1 and (num - 1) not in freq and (num + 1) not in freq:
            result.append(num)

    return result


# Test cases
if __name__ == "__main__":
    # Example 1: Mixed lonely and non-lonely
    nums1 = [10, 6, 5, 8]
    print(f"nums={nums1}: {find_numbers(nums1)}")  # [10, 8]

    # Example 2: All lonely
    nums2 = [1, 3, 5, 7]
    print(f"nums={nums2}: {find_numbers(nums2)}")  # [1, 3, 5, 7]

    # Example 3: Consecutive sequence (none lonely)
    nums3 = [1, 2, 3, 4, 5]
    print(f"nums={nums3}: {find_numbers(nums3)}")  # []

    # Example 4: With duplicates (LeetCode 2150 variant)
    nums4 = [10, 6, 5, 8, 10]
    print(f"nums={nums4} (with freq check): {find_lonely_with_frequency(nums4)}")

    """
    SET LOOKUP PATTERN:

    When to use:
    - Need to check existence of related values (neighbors, complements, etc.)
    - Multiple lookups needed on same data

    Pattern:
    1. Convert array to set: O(n)
    2. For each element, check conditions: O(1) per lookup
    3. Total: O(n) instead of O(n²) with nested loops

    Related problems:
    - Two Sum (check if complement exists)
    - Longest Consecutive Sequence (check neighbors)
    - Contains Duplicate (check if already seen)
    """
