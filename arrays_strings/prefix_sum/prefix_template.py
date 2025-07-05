def fn(arr):
    prefix = [arr[0]]         
    # Step 1: Start the prefix sum array with the first element of input

    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])  
        # Step 2: Add current element to last prefix sum

    return prefix             
    # Step 3: Return the final prefix sum array


print(fn([2,3,5]))  





