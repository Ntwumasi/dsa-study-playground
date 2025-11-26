def combine_two_sorted_arrays(arr1, arr2):
    ans = []
    i = j = 0

    # Merge while both arrays have elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    # Append remaining elements from arr1
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    # Append remaining elements from arr2
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans

print(combine_two_sorted_arrays([1, 5, 8], [2, 3, 4, 6, 7]))