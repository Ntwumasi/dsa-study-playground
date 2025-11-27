"""
Binary Search (LeetCode 704)

PATTERN: Binary Search - Classic Implementation
- Search for target in sorted array
- Return index if found, -1 otherwise

TIME COMPLEXITY: O(log n) - divide search space in half each step
SPACE COMPLEXITY: O(1) - only using pointers

WHY THIS WORKS:
- Array is sorted, so we can determine which half contains target
- Each comparison eliminates half the remaining elements
- log₂(n) comparisons to find answer in array of size n
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Find target in sorted array using binary search.

        Args:
            nums: Sorted array of integers
            target: Value to find

        Returns:
            Index of target, or -1 if not found

        Visual:
            nums = [-1, 0, 3, 5, 9, 12], target = 9

            Step 1: left=0, right=5
                    mid = (0+5)//2 = 2
                    nums[2] = 3 < 9 → search right half

            Step 2: left=3, right=5
                    mid = (3+5)//2 = 4
                    nums[4] = 9 == target ✓

            Return 4
        """
        # Step 1: Initialize pointers at array boundaries
        left = 0
        right = len(nums) - 1

        # Step 2: Continue while search space is valid
        while left <= right:
            # Step 3: Calculate middle index
            # Note: (left + right) // 2 works in Python but can overflow in other languages
            # Safer formula: left + (right - left) // 2
            mid = (left + right) // 2
            num = nums[mid]

            # Step 4: Check if we found the target
            if num == target:
                return mid

            # Step 5: Narrow down the search space
            if num > target:
                # Target must be in left half
                right = mid - 1
            else:
                # Target must be in right half
                left = mid + 1

        # Step 6: Target not found
        return -1


def search_with_comments(nums: list[int], target: int) -> int:
    """
    Same algorithm with detailed trace for learning.
    """
    left = 0
    right = len(nums) - 1
    iteration = 0

    while left <= right:
        iteration += 1
        mid = (left + right) // 2

        print(f"Iteration {iteration}: left={left}, right={right}, mid={mid}, nums[mid]={nums[mid]}")

        if nums[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid
        elif nums[mid] > target:
            print(f"{nums[mid]} > {target}, searching left half")
            right = mid - 1
        else:
            print(f"{nums[mid]} < {target}, searching right half")
            left = mid + 1

    print(f"Target {target} not found")
    return -1


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1: Found
    print(sol.search([-1, 0, 3, 5, 9, 12], 9))  # 4

    # Example 2: Not found
    print(sol.search([-1, 0, 3, 5, 9, 12], 2))  # -1

    # Edge cases
    print(sol.search([5], 5))   # 0 (single element, found)
    print(sol.search([5], -5))  # -1 (single element, not found)
    print(sol.search([], 5))    # -1 (empty array) - would error, need guard

    # Trace example
    print("\n--- Detailed trace ---")
    search_with_comments([1, 3, 5, 7, 9, 11, 13, 15], 11)

    """
    WHY BINARY SEARCH IS O(log n):

    Each iteration halves the search space:
    - n elements → n/2 → n/4 → n/8 → ... → 1

    Number of halvings until we reach 1:
    - n / 2^k = 1
    - n = 2^k
    - k = log₂(n)

    So we do at most log₂(n) iterations!

    Example: n = 1,000,000
    - Linear search: up to 1,000,000 comparisons
    - Binary search: at most 20 comparisons (log₂(1,000,000) ≈ 20)
    """
