"""
Two Sum (LeetCode 1)

PATTERN: Hash Map - Complement Lookup
- For each number, check if its complement (target - num) exists
- Store number -> index mapping for O(1) lookups

TIME COMPLEXITY: O(n) - single pass through array
SPACE COMPLEXITY: O(n) - hash map stores up to n elements

WHY THIS WORKS:
- For two numbers to sum to target: a + b = target
- Rearranged: b = target - a (b is the complement of a)
- Hash map lets us check in O(1) if complement exists
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Find indices of two numbers that add up to target.

    Args:
        nums: Array of integers
        target: Target sum

    Returns:
        List of two indices [i, j] where nums[i] + nums[j] == target

    Visual:
        nums = [2, 7, 11, 15], target = 9

        Build map while scanning:
        i=0: num=2, complement=7, not in map -> map={2: 0}
        i=1: num=7, complement=2, IN MAP at index 0! -> return [1, 0]

        Answer: [1, 0] (or [0, 1] depending on order preference)

    Another example:
        nums = [3, 2, 4], target = 6

        i=0: num=3, complement=3, not in map -> map={3: 0}
        i=1: num=2, complement=4, not in map -> map={3: 0, 2: 1}
        i=2: num=4, complement=2, IN MAP at index 1! -> return [2, 1]

        Answer: [2, 1]
    """
    # Map: number -> index
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num

        # Check if complement was seen before
        if complement in num_to_index:
            return [i, num_to_index[complement]]

        # Store current number and its index
        num_to_index[num] = i

    # Problem guarantees exactly one solution exists
    return []


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force: Check all pairs.

    TIME: O(n²) - nested loops
    SPACE: O(1)

    Simple but inefficient.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_sorted(nums: List[int], target: int) -> List[int]:
    """
    If array were sorted: Two Pointer approach.

    Note: This returns indices in sorted array, not original!
    For original indices, would need to track them.

    TIME: O(n log n) for sorting + O(n) for two pointers
    SPACE: O(n) to store original indices
    """
    # Create pairs of (value, original_index) and sort by value
    indexed = sorted(enumerate(nums), key=lambda x: x[1])

    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = indexed[left][1] + indexed[right][1]

        if current_sum == target:
            return [indexed[left][0], indexed[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []


# Test cases
if __name__ == "__main__":
    # Example 1
    nums1, target1 = [2, 7, 11, 15], 9
    print(f"nums={nums1}, target={target1}: {twoSum(nums1, target1)}")  # [1, 0]

    # Example 2
    nums2, target2 = [3, 2, 4], 6
    print(f"nums={nums2}, target={target2}: {twoSum(nums2, target2)}")  # [2, 1]

    # Example 3: Same number used twice
    nums3, target3 = [3, 3], 6
    print(f"nums={nums3}, target={target3}: {twoSum(nums3, target3)}")  # [1, 0]

    # Compare approaches
    print(f"\nBrute force: {two_sum_brute_force(nums1, target1)}")
    print(f"Sorted approach: {two_sum_sorted(nums1, target1)}")

    """
    TWO SUM VARIATIONS:

    1. Two Sum (this problem): Return indices, unsorted array
       -> Use hash map: O(n) time, O(n) space

    2. Two Sum II - Sorted Array (LeetCode 167): Array is sorted
       -> Use two pointers: O(n) time, O(1) space

    3. Two Sum III - Data Structure Design: Support add() and find()
       -> Use hash map with counts

    4. Two Sum IV - BST: Find pair in BST
       -> In-order traversal + two pointers

    COMPLEMENT LOOKUP PATTERN:

    This pattern extends to many problems:
    - Two Sum: complement = target - num
    - 3Sum: Fix one number, do Two Sum for complement
    - 4Sum: Fix two numbers, do Two Sum for complement
    - Subarray Sum Equals K: complement = prefix_sum - k

    Key insight: Transform "find pair with sum X" into
    "for each element, check if complement exists".
    """
