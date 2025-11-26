# Stacks and Queues

## When to Use

### Stack (LIFO - Last In First Out)
- Matching parentheses/brackets
- Undo operations
- DFS traversal
- Expression evaluation
- Monotonic stack problems

### Queue (FIFO - First In First Out)
- BFS traversal
- Task scheduling
- Sliding window maximum (with deque)

## Visual

### Stack Operations
```
Push 1, Push 2, Push 3, Pop, Push 4

        ┌───┐
        │ 3 │ ← top (pop this)
        ├───┤
        │ 2 │
        ├───┤
        │ 1 │
        └───┘

After Pop:
        ┌───┐
        │ 4 │ ← top (new element)
        ├───┤
        │ 2 │
        ├───┤
        │ 1 │
        └───┘
```

### Valid Parentheses
```
String: "({[]})"

Process:
'(' → push    stack: ['(']
'{' → push    stack: ['(', '{']
'[' → push    stack: ['(', '{', '[']
']' → matches '[', pop   stack: ['(', '{']
'}' → matches '{', pop   stack: ['(']
')' → matches '(', pop   stack: []

Stack empty at end → Valid! ✓
```

### Monotonic Stack (Next Greater Element)
```
Array: [2, 1, 2, 4, 3]
Result: [4, 2, 4, -1, -1]

Traverse right to left, maintain decreasing stack:

i=4: num=3, stack=[]      → result[4]=-1, push 3
     stack: [3]

i=3: num=4, stack=[3]     → 4>3, pop 3
     stack=[], result[3]=-1, push 4
     stack: [4]

i=2: num=2, stack=[4]     → 2<4, result[2]=4, push 2
     stack: [4, 2]

i=1: num=1, stack=[4,2]   → 1<2, result[1]=2, push 1
     stack: [4, 2, 1]

i=0: num=2, stack=[4,2,1] → 2>1, pop; 2>=2, pop
     stack=[4], result[0]=4, push 2
     stack: [4, 2]
```

## Template

### Python
```python
from collections import deque

# Valid parentheses
def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0

# Next greater element (monotonic stack)
def next_greater(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices

    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()

        if stack:
            result[i] = nums[stack[-1]]

        stack.append(i)

    return result

# BFS with queue
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited
```

### TypeScript
```typescript
// Valid parentheses
function isValid(s: string): boolean {
  const stack: string[] = [];
  const pairs: Record<string, string> = {
    ')': '(',
    '}': '{',
    ']': '['
  };

  for (const char of s) {
    if (char in pairs) {
      if (!stack.length || stack[stack.length - 1] !== pairs[char]) {
        return false;
      }
      stack.pop();
    } else {
      stack.push(char);
    }
  }

  return stack.length === 0;
}

// Next greater element (monotonic stack)
function nextGreater(nums: number[]): number[] {
  const n = nums.length;
  const result = new Array(n).fill(-1);
  const stack: number[] = []; // stores indices

  for (let i = n - 1; i >= 0; i--) {
    while (stack.length && nums[stack[stack.length - 1]] <= nums[i]) {
      stack.pop();
    }

    if (stack.length) {
      result[i] = nums[stack[stack.length - 1]];
    }

    stack.push(i);
  }

  return result;
}
```

## Complexity
- **Push/Pop/Peek:** O(1)
- **Space:** O(n) worst case

## Common Problems
- [x] Valid Parentheses
- [x] Simplify Path
- [ ] Min Stack
- [ ] Daily Temperatures
- [ ] Next Greater Element
- [ ] Evaluate Reverse Polish Notation
