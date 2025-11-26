# Binary Search

## When to Use
- Sorted array/space
- Finding boundary (first/last occurrence)
- Search space reduction
- Minimizing/maximizing with constraints

## Visual

### Basic Binary Search
```
Array: [1, 3, 5, 7, 9, 11, 13]   Target: 7

Step 1:  L           M            R
        [1, 3, 5, 7, 9, 11, 13]
                 ↑
              mid=7 == target ✓ Found!

If target < mid: search left half
If target > mid: search right half
```

### Finding Left Boundary (First Occurrence)
```
Array: [1, 2, 2, 2, 3, 4]   Target: 2

Step 1:  L        M        R
        [1, 2, 2, 2, 3, 4]
               ↑
            mid=2 == target, but is it first?
            → move R = mid (keep searching left)

Step 2:  L  M  R
        [1, 2, 2, 2, 3, 4]
            ↑
         mid=2, R = mid

Step 3:  L  R
         M
        [1, 2, 2, 2, 3, 4]
         ↑
        mid=1 < target, L = mid + 1

Step 4:  L
         R
        [1, 2, 2, 2, 3, 4]
            ↑
         L == R, found first 2 at index 1
```

### Search in Rotated Array
```
Array: [4, 5, 6, 7, 0, 1, 2]   Target: 0

        [4, 5, 6, 7, 0, 1, 2]
         L        M        R

mid=7, target=0

Is left half sorted? arr[L]=4 <= arr[M]=7 ✓
Is target in left half? 4 <= 0 <= 7? No
→ Search right half: L = mid + 1

        [4, 5, 6, 7, 0, 1, 2]
                    L  M  R

mid=1, target=0
Is left half sorted? arr[L]=0 <= arr[M]=1 ✓
Is target in left half? 0 <= 0 <= 1? Yes
→ Search left half: R = mid

Continue until found...
```

## Template

### Python
```python
# Basic binary search
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Find left boundary (first occurrence)
def find_left(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left if left < len(nums) and nums[left] == target else -1

# Find right boundary (last occurrence)
def find_right(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left - 1 if left > 0 and nums[left - 1] == target else -1

# Search in rotated sorted array
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

### TypeScript
```typescript
// Basic binary search
function binarySearch(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (nums[mid] === target) {
      return mid;
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1;
}

// Find left boundary (first occurrence)
function findLeft(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length;

  while (left < right) {
    const mid = left + Math.floor((right - left) / 2);

    if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return left < nums.length && nums[left] === target ? left : -1;
}

// Search in rotated sorted array
function searchRotated(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (nums[mid] === target) return mid;

    if (nums[left] <= nums[mid]) {
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    } else {
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }

  return -1;
}
```

## Complexity
- **Time:** O(log n)
- **Space:** O(1) iterative, O(log n) recursive

## Common Problems
- [x] Search in Sorted Array
- [x] Search a 2D Matrix
- [ ] Find First and Last Position
- [ ] Search in Rotated Array
- [ ] Find Minimum in Rotated Array
- [ ] Peak Element
