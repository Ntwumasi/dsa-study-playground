# Two Pointer Pattern

## When to Use
- Searching for pairs in a sorted array
- Comparing elements from both ends
- Removing duplicates in-place
- Partitioning arrays

## Visual

### Opposite Direction (e.g., Two Sum in Sorted Array)
```
Array: [1, 2, 3, 4, 6, 8, 9]
        L              R      Target: 10

Step 1: arr[L] + arr[R] = 1 + 9 = 10 ✓ Found!

        L              R
        ↓              ↓
       [1, 2, 3, 4, 6, 8, 9]

If sum < target: move L right  →
If sum > target: move R left   ←
```

### Same Direction (e.g., Remove Duplicates)
```
Array: [1, 1, 2, 2, 3]
        S
        F

Step 1: arr[S] == arr[F], move F
       [1, 1, 2, 2, 3]
        S  F

Step 2: arr[S] != arr[F], increment S, copy arr[F] to arr[S]
       [1, 2, 2, 2, 3]
           S  F

Continue until F reaches end...

S = Slow pointer (write position)
F = Fast pointer (read position)
```

## Template

### Python
```python
def two_pointer_opposite(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

def two_pointer_same_direction(arr):
    slow = 0

    for fast in range(len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1  # length of unique elements
```

### TypeScript
```typescript
function twoPointerOpposite(arr: number[], target: number): number[] {
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    const currentSum = arr[left] + arr[right];

    if (currentSum === target) {
      return [left, right];
    } else if (currentSum < target) {
      left++;
    } else {
      right--;
    }
  }

  return [];
}

function twoPointerSameDirection(arr: number[]): number {
  let slow = 0;

  for (let fast = 0; fast < arr.length; fast++) {
    if (arr[fast] !== arr[slow]) {
      slow++;
      arr[slow] = arr[fast];
    }
  }

  return slow + 1;
}
```

## Complexity
- **Time:** O(n) - single pass through array
- **Space:** O(1) - no extra space needed

## Common Problems
- [x] Two Sum II (sorted array)
- [x] Reverse String
- [x] Valid Palindrome
- [x] Remove Duplicates from Sorted Array
- [ ] Container With Most Water
- [ ] 3Sum
