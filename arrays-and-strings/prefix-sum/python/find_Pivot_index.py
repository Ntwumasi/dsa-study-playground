"""
Find Pivot Index (LeetCode 724)

PATTERN: Prefix Sum - Running Sum Comparison
- Calculate total sum first
- Track running left sum as we iterate
- At each index, right sum = total - left - current element
- Pivot exists where left sum == right sum

TIME COMPLEXITY: O(n) - two passes (sum + iteration)
SPACE COMPLEXITY: O(1) - only storing sums

WHY THIS WORKS:
- At any index i: leftSum + arr[i] + rightSum = totalSum
- Therefore: rightSum = totalSum - leftSum - arr[i]
- Pivot index is where leftSum == rightSum
"""


class Solution:
    def pivot_index(self, nums: list[int]) -> int:
        """
        Find the pivot index where left sum equals right sum.

        The pivot index is where:
        - Sum of all elements to the LEFT equals
        - Sum of all elements to the RIGHT
        - The element at pivot is NOT included in either sum

        Args:
            nums: Array of integers

        Returns:
            Pivot index, or -1 if none exists

        Visual:
            nums = [1, 7, 3, 6, 5, 6]
            total = 28

            i=0: left=0,  right=28-0-1=27   (0 != 27)
            i=1: left=1,  right=28-1-7=20   (1 != 20)
            i=2: left=8,  right=28-8-3=17   (8 != 17)
            i=3: left=11, right=28-11-6=11  (11 == 11) ✓ FOUND!

            Return 3
        """
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            # Calculate right sum: total - left - current element
            right_sum = total_sum - left_sum - nums[i]

            # Check if this is the pivot
            if left_sum == right_sum:
                return i

            # Add current element to left sum for next iteration
            left_sum += nums[i]

        # No pivot found
        return -1


def pivot_index_alternative(nums: list[int]) -> int:
    """
    Alternative implementation using prefix sum array.

    Less space-efficient but more explicit about the prefix sum pattern.
    """
    if not nums:
        return -1

    n = len(nums)
    total = sum(nums)

    # Build prefix sum
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)

    # Check each potential pivot
    for i in range(n):
        left_sum = prefix[i]              # sum of nums[0..i-1]
        right_sum = total - prefix[i + 1]  # sum of nums[i+1..n-1]

        if left_sum == right_sum:
            return i

    return -1


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1: pivot exists
    print(sol.pivot_index([1, 7, 3, 6, 5, 6]))  # 3
    # Left of index 3: 1+7+3 = 11
    # Right of index 3: 5+6 = 11

    # Example 2: no pivot (return -1)
    print(sol.pivot_index([1, 2, 3]))  # -1
    # No index where left sum equals right sum

    # Example 3: pivot at index 0
    print(sol.pivot_index([2, 1, -1]))  # 0
    # Left of index 0: 0 (empty)
    # Right of index 0: 1+(-1) = 0

    # Edge cases
    print(sol.pivot_index([1]))  # 0 (single element, both sides empty = 0)
    print(sol.pivot_index([]))   # -1 (empty array)

    # Alternative implementation
    print(pivot_index_alternative([1, 7, 3, 6, 5, 6]))  # 3

    """
    KEY INSIGHT:

    Instead of computing left and right sums separately for each index
    (which would be O(n^2)), we use a clever observation:

    rightSum = totalSum - leftSum - nums[i]

    This lets us compute both sums in O(1) at each index!

    We maintain a running leftSum and derive rightSum from the formula.
    Total time: O(n) for sum + O(n) for iteration = O(n)
    """
