def find_max_nums(nums):
    """
    This function takes a list of numbers and returns the maximum number in the list.
    """
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

print(find_max_nums([1, 2, 3, 4, 5]))