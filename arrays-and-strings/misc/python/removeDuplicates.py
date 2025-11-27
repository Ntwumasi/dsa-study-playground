"""
Remove Duplicates from Sorted Array (LeetCode 26)

PATTERN: Two Pointers - Fast/Slow (Read/Write)
- Slow pointer marks position for next unique element
- Fast pointer scans for unique elements
- When unique found, copy to slow position

TIME COMPLEXITY: O(n) - single pass through array
SPACE COMPLEXITY: O(1) - in-place modification

WHY THIS WORKS:
- Array is sorted, so duplicates are adjacent
- Slow pointer always points to last unique element
- Fast pointer finds next unique, we copy it to slow+1
- Elements after return value don't matter
"""

from typing import List


def removeDups(nums: List[int]) -> int:
    """
    Remove duplicates in-place from sorted array.

    Return new length. Elements beyond that can be anything.

    Args:
        nums: Sorted array with possible duplicates

    Returns:
        Length of array with duplicates removed

    Visual:
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

        i=0 (slow/write pointer), j=1 (fast/read pointer)

        j=1: nums[1]=0 == nums[0]=0 -> duplicate, skip
        j=2: nums[2]=1 != nums[0]=0 -> unique!
             i=1, nums[1]=1
             [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]

        j=3: nums[3]=1 == nums[1]=1 -> duplicate, skip
        j=4: nums[4]=1 == nums[1]=1 -> duplicate, skip
        j=5: nums[5]=2 != nums[1]=1 -> unique!
             i=2, nums[2]=2
             [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]

        ... continue ...

        Final: [0, 1, 2, 3, 4, _, _, _, _, _]
        Return: 5 (first 5 elements are unique)
    """
    if not nums:
        return 0

    # i = slow pointer (position of last unique element)
    i = 0

    # j = fast pointer (scanning for new unique elements)
    for j in range(1, len(nums)):
        # Found a new unique element
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    # Length is index + 1
    return i + 1


def remove_duplicates_ii(nums: List[int]) -> int:
    """
    LeetCode 80: Remove Duplicates from Sorted Array II

    Allow at most 2 duplicates of each element.

    Visual:
        nums = [1, 1, 1, 2, 2, 3]
        Result: [1, 1, 2, 2, 3] -> return 5
    """
    if len(nums) <= 2:
        return len(nums)

    # i = write pointer, start at 2 (first two always kept)
    i = 2

    for j in range(2, len(nums)):
        # Check against element two positions back
        # If different, this is at most the second duplicate
        if nums[j] != nums[i - 2]:
            nums[i] = nums[j]
            i += 1

    return i


def remove_element(nums: List[int], val: int) -> int:
    """
    LeetCode 27: Remove Element

    Remove all occurrences of val in-place.

    Visual:
        nums = [3, 2, 2, 3], val = 3
        Result: [2, 2] -> return 2
    """
    i = 0  # Write pointer

    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1

    return i


# Test cases
if __name__ == "__main__":
    # Example 1
    nums1 = [1, 1, 2]
    length1 = removeDups(nums1)
    print(f"[1,1,2] -> {nums1[:length1]}, length={length1}")  # [1, 2], 2

    # Example 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length2 = removeDups(nums2)
    print(f"[0,0,1,1,1,2,2,3,3,4] -> {nums2[:length2]}, length={length2}")
    # [0, 1, 2, 3, 4], 5

    # Example 3: All same
    nums3 = [1, 1, 1, 1]
    length3 = removeDups(nums3)
    print(f"[1,1,1,1] -> {nums3[:length3]}, length={length3}")  # [1], 1

    # Example 4: No duplicates
    nums4 = [1, 2, 3]
    length4 = removeDups(nums4)
    print(f"[1,2,3] -> {nums4[:length4]}, length={length4}")  # [1, 2, 3], 3

    # Remove Duplicates II
    print("\nRemove Duplicates II (allow 2):")
    nums5 = [1, 1, 1, 2, 2, 3]
    length5 = remove_duplicates_ii(nums5)
    print(f"[1,1,1,2,2,3] -> {nums5[:length5]}, length={length5}")  # [1,1,2,2,3], 5

    # Remove Element
    print("\nRemove Element:")
    nums6 = [3, 2, 2, 3]
    length6 = remove_element(nums6, 3)
    print(f"[3,2,2,3] remove 3 -> {nums6[:length6]}, length={length6}")  # [2, 2], 2

    """
    FAST/SLOW POINTER PATTERN:

    Used for in-place array modifications:
    - Slow = write position (where to put next valid element)
    - Fast = read position (scanning for valid elements)

    Template:
        slow = 0 (or starting position)
        for fast in range(start, len(arr)):
            if is_valid(arr[fast]):
                arr[slow] = arr[fast]
                slow += 1
        return slow

    VARIATIONS:

    1. Remove duplicates (keep 1): Compare with nums[slow]
    2. Remove duplicates (keep k): Compare with nums[slow - k]
    3. Remove element: Check if nums[fast] != val
    4. Move zeros: Check if nums[fast] != 0

    KEY INSIGHT:
    Elements before slow pointer are all "valid" (kept)
    Elements at slow and beyond may be overwritten
    Return value is the count of valid elements
    """
