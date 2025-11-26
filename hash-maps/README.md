# Hash Maps

## When to Use
- O(1) lookup for existence checks
- Counting frequencies
- Grouping/categorizing elements
- Finding pairs with specific relationships
- Caching/memoization

## Visual

### Frequency Counter
```
String: "aabbbcc"

Building frequency map:

'a' → count: 1      {'a': 1}
'a' → count: 2      {'a': 2}
'b' → count: 1      {'a': 2, 'b': 1}
'b' → count: 2      {'a': 2, 'b': 2}
'b' → count: 3      {'a': 2, 'b': 3}
'c' → count: 1      {'a': 2, 'b': 3, 'c': 1}
'c' → count: 2      {'a': 2, 'b': 3, 'c': 2}

Final: {'a': 2, 'b': 3, 'c': 2}
```

### Two Sum with Hash Map
```
Array: [2, 7, 11, 15]   Target: 9

seen = {}

i=0: num=2, need=7, 7 not in seen, add {2: 0}
i=1: num=7, need=2, 2 in seen! ✓

Return [seen[2], i] = [0, 1]

Hash map enables O(1) complement lookup!
```

### Grouping by Key (Anagrams)
```
Words: ["eat", "tea", "tan", "ate", "nat", "bat"]

Sort each word → use as key:

"eat" → "aet" → {"aet": ["eat"]}
"tea" → "aet" → {"aet": ["eat", "tea"]}
"tan" → "ant" → {"aet": [...], "ant": ["tan"]}
"ate" → "aet" → {"aet": ["eat", "tea", "ate"], ...}
"nat" → "ant" → {"aet": [...], "ant": ["tan", "nat"]}
"bat" → "abt" → {..., "abt": ["bat"]}

Result: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
```

## Template

### Python
```python
from collections import defaultdict, Counter

# Frequency counter
def count_freq(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Or using Counter
def count_freq_counter(arr):
    return Counter(arr)

# Two Sum
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Group anagrams
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```

### TypeScript
```typescript
// Frequency counter
function countFreq(arr: string[]): Map<string, number> {
  const freq = new Map<string, number>();
  for (const item of arr) {
    freq.set(item, (freq.get(item) || 0) + 1);
  }
  return freq;
}

// Two Sum
function twoSum(nums: number[], target: number): number[] {
  const seen = new Map<number, number>();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (seen.has(complement)) {
      return [seen.get(complement)!, i];
    }
    seen.set(nums[i], i);
  }
  return [];
}

// Group anagrams
function groupAnagrams(strs: string[]): string[][] {
  const groups = new Map<string, string[]>();
  for (const s of strs) {
    const key = s.split('').sort().join('');
    if (!groups.has(key)) {
      groups.set(key, []);
    }
    groups.get(key)!.push(s);
  }
  return Array.from(groups.values());
}
```

## Complexity
- **Insert/Lookup/Delete:** O(1) average
- **Space:** O(n) for n unique elements

## Common Problems
- [x] Two Sum
- [x] Ransom Note
- [x] Check if Pangram
- [x] Find Winners and Losers
- [ ] Group Anagrams
- [ ] Valid Anagram
- [ ] Longest Consecutive Sequence
