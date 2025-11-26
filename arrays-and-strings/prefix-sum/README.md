# Prefix Sum Pattern

## When to Use
- Range sum queries
- Finding subarrays with a target sum
- Counting subarrays with specific properties
- Problems asking about cumulative values

## Visual

### Building Prefix Sum Array
```
Original:    [1, 2, 3, 4, 5]
              ↓  ↓  ↓  ↓  ↓
Prefix Sum: [1, 3, 6, 10, 15]

prefix[i] = sum of all elements from index 0 to i

prefix[0] = 1
prefix[1] = 1 + 2 = 3
prefix[2] = 1 + 2 + 3 = 6
prefix[3] = 1 + 2 + 3 + 4 = 10
prefix[4] = 1 + 2 + 3 + 4 + 5 = 15
```

### Range Sum Query
```
Array:      [1, 2, 3, 4, 5]
Prefix:     [1, 3, 6, 10, 15]

Q: Sum from index 1 to 3?  (elements: 2, 3, 4)

            [1, 2, 3, 4, 5]
                ↑     ↑
               L=1   R=3

Answer = prefix[R] - prefix[L-1]
       = prefix[3] - prefix[0]
       = 10 - 1 = 9  ✓

       (2 + 3 + 4 = 9)
```

### Find Pivot Index
```
Array: [1, 7, 3, 6, 5, 6]

Total sum = 28

Index 0: left=0,  right=27  ✗
Index 1: left=1,  right=20  ✗
Index 2: left=8,  right=17  ✗
Index 3: left=11, right=11  ✓  Pivot found!

         [1, 7, 3, 6, 5, 6]
                   ↑
               pivot (index 3)

         left sum = 1+7+3 = 11
         right sum = 5+6 = 11
```

## Template

### Python
```python
# Build prefix sum
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

# Range sum query (L to R inclusive)
def range_sum(prefix, L, R):
    return prefix[R + 1] - prefix[L]

# Find pivot index
def pivot_index(nums):
    total = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        right_sum = total - left_sum - num
        if left_sum == right_sum:
            return i
        left_sum += num

    return -1

# Running sum
def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
```

### TypeScript
```typescript
// Build prefix sum
function buildPrefix(arr: number[]): number[] {
  const prefix = new Array(arr.length + 1).fill(0);
  for (let i = 0; i < arr.length; i++) {
    prefix[i + 1] = prefix[i] + arr[i];
  }
  return prefix;
}

// Range sum query (L to R inclusive)
function rangeSum(prefix: number[], L: number, R: number): number {
  return prefix[R + 1] - prefix[L];
}

// Find pivot index
function pivotIndex(nums: number[]): number {
  const total = nums.reduce((a, b) => a + b, 0);
  let leftSum = 0;

  for (let i = 0; i < nums.length; i++) {
    const rightSum = total - leftSum - nums[i];
    if (leftSum === rightSum) {
      return i;
    }
    leftSum += nums[i];
  }

  return -1;
}

// Running sum
function runningSum(nums: number[]): number[] {
  for (let i = 1; i < nums.length; i++) {
    nums[i] += nums[i - 1];
  }
  return nums;
}
```

## Complexity
- **Build:** O(n) time, O(n) space
- **Query:** O(1) time
- **Space optimization:** Can modify in-place for running sum

## Common Problems
- [x] Running Sum of 1D Array
- [x] Find Pivot Index
- [x] Number of Ways to Split Array
- [ ] Subarray Sum Equals K
- [ ] Product of Array Except Self
- [ ] Continuous Subarray Sum
