"""
Running Sum of 1D Array (LeetCode 1480)

PATTERN: Prefix Sum - Basic Building Block
- Transform array where each element becomes cumulative sum up to that point
- runningSum[i] = sum(nums[0..i])

TIME COMPLEXITY: O(n) - single pass
SPACE COMPLEXITY: O(n) for result, or O(1) if modifying in-place

WHY THIS WORKS:
- Each new running sum = previous running sum + current element
- runningSum[i] = runningSum[i-1] + nums[i]
- This is the foundation of the prefix sum technique
"""


class Solution:
    def running_sum(self, nums: list[int]) -> list[int]:
        """
        Calculate the running sum of an array.

        Args:
            nums: Array of integers

        Returns:
            Array where each element is the cumulative sum

        Visual:
            nums = [1, 2, 3, 4]

            runningSum[0] = 1                    = 1
            runningSum[1] = 1 + 2                = 3
            runningSum[2] = 1 + 2 + 3            = 6
            runningSum[3] = 1 + 2 + 3 + 4        = 10

            Result: [1, 3, 6, 10]
        """
        if not nums:
            return []

        # Start with first element
        prefix = [nums[0]]

        # Build running sum
        for i in range(1, len(nums)):
            # Each element = previous sum + current number
            prefix.append(prefix[-1] + nums[i])

        return prefix


def running_sum_inplace(nums: list[int]) -> list[int]:
    """
    In-place modification (modifies original array).

    More space-efficient if you don't need the original array.
    """
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


def running_sum_pythonic(nums: list[int]) -> list[int]:
    """
    Pythonic solution using itertools.accumulate.
    """
    from itertools import accumulate
    return list(accumulate(nums))


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.running_sum([1, 2, 3, 4]))  # [1, 3, 6, 10]

    # Example 2
    print(sol.running_sum([1, 1, 1, 1, 1]))  # [1, 2, 3, 4, 5]

    # Example 3
    print(sol.running_sum([3, 1, 2, 10, 1]))  # [3, 4, 6, 16, 17]

    # Edge cases
    print(sol.running_sum([5]))  # [5]
    print(sol.running_sum([]))   # []

    # Pythonic version
    print(running_sum_pythonic([1, 2, 3, 4]))  # [1, 3, 6, 10]

    """
    THIS IS THE BUILDING BLOCK:

    Running sum (prefix sum) is fundamental because it enables:

    1. O(1) range sum queries:
       sum(nums[i..j]) = prefix[j] - prefix[i-1]

    2. Subarray sum problems:
       - Find subarray with sum = k
       - Count subarrays with sum <= k

    3. Split/partition problems:
       - Valid splits where left sum >= right sum
       - Find pivot index

    4. Difference array (inverse of prefix sum):
       - Efficient range updates

    Master this pattern - it appears EVERYWHERE in DSA!
    """
