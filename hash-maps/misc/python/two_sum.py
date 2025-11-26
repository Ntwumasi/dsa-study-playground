def twosum(nums, target):
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in dic:
            return [i, dic[complement]]

        dic[num] = i