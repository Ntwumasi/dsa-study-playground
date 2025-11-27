"""
Merge Two Sorted Arrays (Foundation for LeetCode 88)

PATTERN: Two Pointer - Same Direction on Two Arrays
- Use one pointer for each array
- Compare elements, take the smaller one
- Continue until both arrays are exhausted

TIME COMPLEXITY: O(n + m) where n, m are lengths of the two arrays
SPACE COMPLEXITY: O(n + m) for the result array

WHY THIS WORKS:
- Both arrays are already sorted
- At each step, the smallest remaining element is at one of the two pointers
- By always taking the smaller one, we maintain sorted order in result
"""


def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Merge two sorted arrays into one sorted array.

    Args:
        arr1: First sorted array
        arr2: Second sorted array

    Returns:
        Merged sorted array

    Visual:
        arr1 = [1, 5, 8]
        arr2 = [2, 3, 4, 6, 7]

        Step 1: 1 < 2 → take 1, result=[1]
        Step 2: 5 > 2 → take 2, result=[1, 2]
        Step 3: 5 > 3 → take 3, result=[1, 2, 3]
        Step 4: 5 > 4 → take 4, result=[1, 2, 3, 4]
        Step 5: 5 < 6 → take 5, result=[1, 2, 3, 4, 5]
        Step 6: 8 > 6 → take 6, result=[1, 2, 3, 4, 5, 6]
        Step 7: 8 > 7 → take 7, result=[1, 2, 3, 4, 5, 6, 7]
        Step 8: arr2 exhausted, append 8 → result=[1, 2, 3, 4, 5, 6, 7, 8]
    """
    result = []
    i = j = 0  # Pointers for arr1 and arr2

    # Compare elements while both arrays have elements remaining
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Append any remaining elements from arr1
    # (only one of these while loops will execute)
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # Append any remaining elements from arr2
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


def merge_sorted_arrays_pythonic(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Alternative: Use Python's extend for remaining elements.
    Same complexity, slightly cleaner code.
    """
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Extend with remaining elements (slicing creates a copy)
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result


# Test cases
if __name__ == "__main__":
    print(merge_sorted_arrays([1, 5, 8], [2, 3, 4, 6, 7]))
    # [1, 2, 3, 4, 5, 6, 7, 8]

    print(merge_sorted_arrays([1, 2, 3], [4, 5, 6]))
    # [1, 2, 3, 4, 5, 6] - no interleaving needed

    print(merge_sorted_arrays([], [1, 2, 3]))
    # [1, 2, 3] - one empty array

    print(merge_sorted_arrays([1], [1]))
    # [1, 1] - duplicates allowed
