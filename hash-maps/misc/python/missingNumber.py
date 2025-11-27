"""
Missing Number (LeetCode 268)

PATTERN: Hash Set / Math Formula / XOR
- Given n numbers from range [0, n], find the missing one
- Multiple approaches: set lookup, math sum, XOR

TIME COMPLEXITY: O(n) for all approaches
SPACE COMPLEXITY: O(n) for set, O(1) for math/XOR

WHY THIS WORKS:
- Set: Convert to set, check which number in [0,n] is missing
- Math: Sum of 0 to n is n*(n+1)/2, subtract actual sum
- XOR: a^a=0, so XOR all indices and values cancels pairs
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Find the missing number in [0, n] range.

        Args:
            nums: Array of n distinct numbers from [0, n]

        Returns:
            The one missing number

        Visual (Set approach):
            nums = [3, 0, 1]
            n = 3, so range is [0, 1, 2, 3]

            nums_set = {3, 0, 1}

            Check each number in range:
            - 0 in set? Yes
            - 1 in set? Yes
            - 2 in set? No -> MISSING!
            - 3 in set? Yes

            Answer: 2
        """
        nums_set = set(nums)
        n = len(nums)

        # Check which number from [0, n] is missing
        for i in range(n + 1):
            if i not in nums_set:
                return i

        return -1  # Should never reach here


def missing_number_math(nums: List[int]) -> int:
    """
    Math approach using Gauss formula.

    Sum of 0 to n = n * (n + 1) / 2
    Missing = expected sum - actual sum

    TIME: O(n), SPACE: O(1)

    Visual:
        nums = [3, 0, 1], n = 3
        Expected sum = 3 * 4 / 2 = 6
        Actual sum = 3 + 0 + 1 = 4
        Missing = 6 - 4 = 2
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def missing_number_xor(nums: List[int]) -> int:
    """
    XOR approach using property: a ^ a = 0.

    XOR all indices [0, n] with all values in nums.
    Pairs cancel out, leaving only the missing number.

    TIME: O(n), SPACE: O(1)

    Visual:
        nums = [3, 0, 1], n = 3

        XOR indices: 0 ^ 1 ^ 2 ^ 3 = some value
        XOR values:  3 ^ 0 ^ 1 = some value

        Combined: 0^1^2^3 ^ 3^0^1
                = (0^0) ^ (1^1) ^ (3^3) ^ 2
                = 0 ^ 0 ^ 0 ^ 2
                = 2

        Each number except 2 appears twice (cancels out).
    """
    n = len(nums)
    result = n  # Start with n (the last index)

    for i in range(n):
        # XOR with both index and value
        result ^= i ^ nums[i]

    return result


def missing_number_sort(nums: List[int]) -> int:
    """
    Sort approach (original implementation).

    TIME: O(n log n) - dominated by sorting
    SPACE: O(1) or O(n) depending on sort implementation

    Less efficient but intuitive.
    """
    nums.sort()

    # Check if n is missing (should be at last index)
    if nums[-1] != len(nums):
        return len(nums)

    # Check if 0 is missing
    if nums[0] != 0:
        return 0

    # Check for gap in sequence
    for i in range(1, len(nums)):
        expected = nums[i - 1] + 1
        if nums[i] != expected:
            return expected

    return -1


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums1 = [3, 0, 1]
    print(f"nums={nums1}: {sol.missingNumber(nums1)}")  # 2

    # Example 2
    nums2 = [0, 1]
    print(f"nums={nums2}: {sol.missingNumber(nums2)}")  # 2

    # Example 3
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(f"nums={nums3}: {sol.missingNumber(nums3)}")  # 8

    # Compare approaches
    print(f"\nMath approach: {missing_number_math(nums1)}")  # 2
    print(f"XOR approach: {missing_number_xor(nums1)}")  # 2
    print(f"Sort approach: {missing_number_sort(nums1)}")  # 2

    """
    APPROACH COMPARISON:

    | Approach | Time    | Space | Notes                        |
    |----------|---------|-------|------------------------------|
    | Set      | O(n)    | O(n)  | Simple, clear logic          |
    | Math     | O(n)    | O(1)  | Risk of overflow for large n |
    | XOR      | O(n)    | O(1)  | Clever, no overflow risk     |
    | Sort     | O(nlogn)| O(1)  | Simple but slower            |

    XOR TRICK EXPLAINED:
    - XOR is commutative: a^b = b^a
    - XOR is associative: (a^b)^c = a^(b^c)
    - Self-inverse: a^a = 0
    - Identity: a^0 = a

    So XOR-ing all indices and values leaves only unpaired number.
    """
