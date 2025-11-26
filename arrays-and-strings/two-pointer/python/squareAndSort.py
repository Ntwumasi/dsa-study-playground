def square_and_sort(nums):
    results = []
    for num in nums:
        square = num ** 2
        results.append(square)
    results.sort()
    
    return results