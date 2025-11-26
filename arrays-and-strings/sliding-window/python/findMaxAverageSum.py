find maxAverageSum(nums, k):
    window_sum = sum(nums[:k])
    # this gives us the length of the current/starting window
    max_sum = window_sum
    # we will say the max_sum right now to start is the length
    # of the window we are looking at
    for i in range(k,len(nums)):
        outgoing = nums[i-k]
        incoming = nums[i]

        window_sum = window_sum - outgoing + incoming
        max_sum = max(window_sum, max_sum)

        average_sum = max_sum / k

    return average_sum
        