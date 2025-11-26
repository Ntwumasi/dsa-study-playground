# Sliding Window Pattern

## When to Use
- Finding subarrays/substrings with specific properties
- Maximum/minimum sum of k consecutive elements
- Longest/shortest substring with certain conditions
- Problems involving contiguous sequences

## Visual

### Fixed Window (e.g., Max Sum of K Elements)
```
Array: [2, 1, 5, 1, 3, 2]    k = 3

Window slides right →

Step 1: [2, 1, 5] 1, 3, 2    sum = 8
         └──┬──┘
           window

Step 2:  2 [1, 5, 1] 3, 2    sum = 8 - 2 + 1 = 7
            └──┬──┘
              window

Step 3:  2, 1 [5, 1, 3] 2    sum = 7 - 1 + 3 = 8
               └──┬──┘
                 window

Step 4:  2, 1, 5 [1, 3, 2]   sum = 8 - 5 + 2 = 6
                  └──┬──┘
                    window

Max sum = 8
```

### Dynamic Window (e.g., Longest Substring Without Repeats)
```
String: "abcabcbb"

         L
         R
        [a] b c a b c b b     window = {a}, len = 1

         L
            R
        [a  b] c a b c b b    window = {a,b}, len = 2

         L
               R
        [a  b  c] a b c b b   window = {a,b,c}, len = 3

               L              'a' repeats! shrink from left
               R
         a  b [c  a] b c b b  window = {c,a}, len = 2

Continue expanding until invalid, then shrink...
```

## Template

### Python
```python
# Fixed window
def fixed_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # slide: add new, remove old
        max_sum = max(max_sum, window_sum)

    return max_sum

# Dynamic window
def dynamic_window(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

### TypeScript
```typescript
// Fixed window
function fixedWindow(arr: number[], k: number): number {
  let windowSum = arr.slice(0, k).reduce((a, b) => a + b, 0);
  let maxSum = windowSum;

  for (let i = k; i < arr.length; i++) {
    windowSum += arr[i] - arr[i - k];
    maxSum = Math.max(maxSum, windowSum);
  }

  return maxSum;
}

// Dynamic window
function dynamicWindow(s: string): number {
  const seen = new Set<string>();
  let left = 0;
  let maxLength = 0;

  for (let right = 0; right < s.length; right++) {
    while (seen.has(s[right])) {
      seen.delete(s[left]);
      left++;
    }

    seen.add(s[right]);
    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
}
```

## Complexity
- **Time:** O(n) - each element visited at most twice
- **Space:** O(1) for fixed, O(k) for dynamic (where k = window size or unique elements)

## Common Problems
- [x] Maximum Average Subarray
- [x] Longest Substring Without Repeating Characters
- [x] Max Consecutive Ones III
- [ ] Minimum Window Substring
- [ ] Permutation in String
- [ ] Fruit Into Baskets
