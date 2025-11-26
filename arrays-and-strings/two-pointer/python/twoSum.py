def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return [left + 1, right + 1]  # 1-based indexing
        elif curr < target:
            left += 1
        else:
            right -= 1
    return None