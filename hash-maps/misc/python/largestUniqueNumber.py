"""
Largest Unique Number (LeetCode 1133)

PATTERN: Hash Map - Frequency Counting
- Count frequency of each number
- Find largest number with frequency exactly 1

TIME COMPLEXITY: O(n) - single pass to count + O(n) to find max
SPACE COMPLEXITY: O(n) - hash map for frequencies

WHY THIS WORKS:
- Counter gives us frequency of each number in O(n)
- Filter for frequency == 1, then find max
- If no unique number exists, return -1
"""

from collections import Counter
from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        """
        Find the largest number that appears exactly once.

        Args:
            nums: Array of integers

        Returns:
            Largest unique number, or -1 if none exists

        Visual:
            nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]

            Frequency count:
            {5: 1, 7: 1, 3: 2, 9: 2, 4: 1, 8: 1, 1: 1}

            Filter freq == 1:
            [5, 7, 4, 8, 1]

            Max of these: 8

            Answer: 8

        Example 2:
            nums = [9, 9, 8, 8]
            All numbers appear twice -> no unique numbers
            Answer: -1
        """
        # Count frequencies of all numbers
        frequency_map = Counter(nums)

        # Find the largest number with frequency 1
        # Generator expression filters to unique numbers only
        return max(
            (num for num, freq in frequency_map.items() if freq == 1),
            default=-1,  # Return -1 if no unique numbers
        )


def largest_unique_manual(nums: List[int]) -> int:
    """
    Alternative: Manual implementation without Counter.

    Shows the underlying hash map logic.
    """
    # Build frequency map
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Find largest unique
    result = -1
    for num, count in freq.items():
        if count == 1:
            result = max(result, num)

    return result


def largest_unique_sorted(nums: List[int]) -> int:
    """
    Alternative: Sort and scan approach.

    TIME: O(n log n) due to sorting
    SPACE: O(1) if sorting in-place (ignoring sort's internal space)

    Less efficient but doesn't require extra hash map space.
    """
    if not nums:
        return -1

    nums.sort(reverse=True)  # Sort descending

    i = 0
    while i < len(nums):
        # Count consecutive duplicates
        count = 1
        while i + count < len(nums) and nums[i] == nums[i + count]:
            count += 1

        # If this number appears exactly once, it's our answer
        if count == 1:
            return nums[i]

        # Skip all duplicates
        i += count

    return -1


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1: Multiple unique numbers
    nums1 = [5, 7, 3, 9, 4, 9, 8, 3, 1]
    print(f"nums={nums1}: {sol.largestUniqueNumber(nums1)}")  # 8

    # Example 2: No unique numbers
    nums2 = [9, 9, 8, 8]
    print(f"nums={nums2}: {sol.largestUniqueNumber(nums2)}")  # -1

    # Example 3: All unique
    nums3 = [1, 2, 3]
    print(f"nums={nums3}: {sol.largestUniqueNumber(nums3)}")  # 3

    # Alternative approaches
    print(f"Manual approach: {largest_unique_manual(nums1)}")  # 8
    print(f"Sorted approach: {largest_unique_sorted(nums1)}")  # 8

    """
    FREQUENCY COUNTING PATTERN:

    Common applications:
    1. Find elements with specific frequency (unique, duplicates, etc.)
    2. Find most/least common elements
    3. Check if two strings are anagrams
    4. Group elements by frequency

    Counter vs manual dict:
    - Counter: cleaner syntax, has most_common() method
    - Manual dict: more explicit, sometimes needed for custom logic

    Related problems:
    - First Unique Character in a String
    - Top K Frequent Elements
    - Sort Characters By Frequency
    """
