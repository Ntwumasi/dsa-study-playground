"""
Number of Ways to Split Array (LeetCode 2270)

PATTERN: Prefix Sum - Array Splitting
- A valid split at index i means: sum(arr[0..i]) >= sum(arr[i+1..n-1])
- Use prefix sum to compute left and right sums efficiently
- Count splits where left >= right

TIME COMPLEXITY: O(n) - build prefix + single pass
SPACE COMPLEXITY: O(1) if optimized, O(n) with explicit prefix array

WHY THIS WORKS:
- With prefix sum, we can get any range sum in O(1)
- At split index i: leftSum = prefix[i+1], rightSum = total - leftSum
- Check condition and count valid splits
"""


class Solution:
    def ways_to_split_array(self, nums: list[int]) -> int:
        """
        Count valid ways to split array where left sum >= right sum.

        A split at index i divides array into:
        - Left part: nums[0..i]
        - Right part: nums[i+1..n-1]

        Valid split: sum(left part) >= sum(right part)

        Args:
            nums: Array of integers

        Returns:
            Number of valid splits

        Visual:
            nums = [10, 4, -8, 7]

            Split at i=0: left=[10], right=[4,-8,7]
                         leftSum=10, rightSum=3
                         10 >= 3 ✓ valid

            Split at i=1: left=[10,4], right=[-8,7]
                         leftSum=14, rightSum=-1
                         14 >= -1 ✓ valid

            Split at i=2: left=[10,4,-8], right=[7]
                         leftSum=6, rightSum=7
                         6 >= 7 ✗ invalid

            Note: Can't split at i=3 (right part would be empty)

            Answer: 2
        """
        n = len(nums)

        # Build prefix sum with leading zero
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        total = prefix[n]  # Total sum of array
        count = 0

        # Try each valid split point (can't split at last index)
        for i in range(n - 1):
            left_sum = prefix[i + 1]          # sum of nums[0..i]
            right_sum = total - left_sum      # sum of nums[i+1..n-1]

            if left_sum >= right_sum:
                count += 1

        return count


def ways_to_split_array_optimized(nums: list[int]) -> int:
    """
    Space-optimized version without explicit prefix array.

    Instead of storing entire prefix array, maintain running sum.
    """
    total = sum(nums)
    left_sum = 0
    count = 0

    # Iterate through valid split points (0 to n-2)
    for i in range(len(nums) - 1):
        left_sum += nums[i]
        right_sum = total - left_sum

        if left_sum >= right_sum:
            count += 1

    return count


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.ways_to_split_array([10, 4, -8, 7]))  # 2

    # Example 2
    print(sol.ways_to_split_array([2, 3, 1, 0]))   # 2
    # Split at 0: [2] vs [3,1,0]=4 -> 2 >= 4? No
    # Split at 1: [2,3]=5 vs [1,0]=1 -> 5 >= 1? Yes
    # Split at 2: [2,3,1]=6 vs [0] -> 6 >= 0? Yes

    # Edge cases
    print(sol.ways_to_split_array([1, 1]))         # 1 (only one split possible)
    print(sol.ways_to_split_array([0, 0]))         # 1 (0 >= 0)

    # Optimized version
    print(ways_to_split_array_optimized([10, 4, -8, 7]))  # 2

    """
    RELATIONSHIP TO PREFIX SUM:

    This problem demonstrates how prefix sums enable efficient "split" queries:

    Given array: [a, b, c, d, e]
    Prefix:      [0, a, a+b, a+b+c, a+b+c+d, a+b+c+d+e]
                     ^              ^         ^total

    Split at index 1:
    - Left sum = prefix[2] = a + b
    - Right sum = total - prefix[2] = c + d + e

    This O(1) lookup per split point gives us O(n) total!
    """
