"""
Merge Sorted Array (LeetCode 88)

PATTERN: Three Pointers - Merge from End
- nums1 has extra space at the end
- Start merging from the largest elements (end)
- Place larger element at the back of nums1

TIME COMPLEXITY: O(m + n) - single pass through both arrays
SPACE COMPLEXITY: O(1) - in-place merge

WHY THIS WORKS:
- Merging from end avoids overwriting elements we still need
- The extra space in nums1 is at the end, so we fill it first
- Larger elements go to the back, smaller stay in front
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 in-place.

        nums1 has length m + n, with first m elements to merge
        and last n elements as zeros (placeholder space).

        Args:
            nums1: First sorted array with extra space
            m: Number of valid elements in nums1
            nums2: Second sorted array
            n: Number of elements in nums2

        Visual:
            nums1 = [1, 2, 3, 0, 0, 0], m = 3
            nums2 = [2, 5, 6], n = 3

            Pointers: i=2 (nums1[2]=3), j=2 (nums2[2]=6), k=5 (end)

            Step 1: 3 < 6 -> nums1[5] = 6, j=1, k=4
                    [1, 2, 3, 0, 0, 6]

            Step 2: 3 < 5 -> nums1[4] = 5, j=0, k=3
                    [1, 2, 3, 0, 5, 6]

            Step 3: 3 > 2 -> nums1[3] = 3, i=1, k=2
                    [1, 2, 3, 3, 5, 6]

            Step 4: 2 = 2 -> nums1[2] = 2, j=-1, k=1
                    [1, 2, 2, 3, 5, 6]

            j < 0, done! (remaining nums1 elements already in place)

            Result: [1, 2, 2, 3, 5, 6]
        """
        # Three pointers: end of valid nums1, end of nums2, write position
        i = m - 1      # Last valid element in nums1
        j = n - 1      # Last element in nums2
        k = m + n - 1  # Write position (end of nums1)

        # Merge from the end, placing larger elements first
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements remain in nums2, copy them
        # (No need to handle remaining nums1 - they're already in place)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


def merge_from_start(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Alternative: Merge from start (requires extra space).

    TIME: O(m + n), SPACE: O(m)

    Copy nums1 first, then merge like standard merge sort.
    """
    # Make a copy of nums1's valid elements
    nums1_copy = nums1[:m]

    # Three pointers
    i = 0  # pointer for nums1_copy
    j = 0  # pointer for nums2
    k = 0  # write pointer for nums1

    while i < m and j < n:
        if nums1_copy[i] <= nums2[j]:
            nums1[k] = nums1_copy[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        k += 1

    # Copy remaining elements
    while i < m:
        nums1[k] = nums1_copy[i]
        i += 1
        k += 1

    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    sol.merge(nums1, 3, nums2, 3)
    print(f"Merged: {nums1}")  # [1, 2, 2, 3, 5, 6]

    # Example 2: nums2 is empty
    nums1 = [1]
    nums2 = []
    sol.merge(nums1, 1, nums2, 0)
    print(f"Empty nums2: {nums1}")  # [1]

    # Example 3: nums1 is empty (only zeros)
    nums1 = [0]
    nums2 = [1]
    sol.merge(nums1, 0, nums2, 1)
    print(f"Empty nums1: {nums1}")  # [1]

    # Example 4: All nums2 smaller than nums1
    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    sol.merge(nums1, 3, nums2, 3)
    print(f"All smaller: {nums1}")  # [1, 2, 3, 4, 5, 6]

    """
    WHY MERGE FROM END?

    If we merge from the start:
    - We'd overwrite elements in nums1 that we still need
    - Would need extra space to store nums1's elements

    From the end:
    - The "empty" space (zeros) is at the end
    - We fill this space with largest elements first
    - nums1's elements we still need are safe in front

    MERGE FROM END PATTERN:

    Use when:
    - One array has extra space at the end
    - Need to merge in-place

    Pattern:
        i = end of array1 valid elements
        j = end of array2
        k = end of total space

        while both have elements:
            pick larger, place at k, decrement

    RELATED PROBLEMS:
    - Merge Two Sorted Lists (linked lists version)
    - Sort Colors (Dutch National Flag - 3-way partition)
    - Intersection of Two Arrays
    """
