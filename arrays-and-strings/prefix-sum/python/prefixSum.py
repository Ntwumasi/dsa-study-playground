# Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit,
# return a boolean array that represents the 
# answer to each query. A query is true if the sum of the subarray from x to y is less than limit,
# or false otherwise.

def answer_queries(nums, queries, limit):
    prefix = [nums[0]] # adding the first element to the prefix sum
    for i in range(1, len(nums)): # looping through the rest of the elements
        prefix.append(nums[i] + prefix[-1]) # adding the current element to the last element of the prefix sum
    
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans