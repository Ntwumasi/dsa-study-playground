class Solution:
    def search(self, nums: [int], target: int) -> int:
        # Step 1: Initialize two pointers at the start and end of the array
        left = 0
        right = len(nums) - 1

        # Step 2: Keep searching as long as the search space is valid
        while left <= right:
            # Step 3: Find the middle index (not the average of values, but average index)
            mid = (left + right) // 2
            num = nums[mid]  # Step 4: Get the element at the middle index

            # Step 5: If it's a match, return the index
            if num == target:
                return mid

            # Step 6: If middle value is too big, move the right pointer
            if num > target:
                right = mid - 1
            else:
                # Step 7: If middle value is too small, move the left pointer
                left = mid + 1

        # Step 8: If the loop ends, the target was not found
        return -1