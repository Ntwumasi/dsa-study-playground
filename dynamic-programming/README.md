# Dynamic Programming

## When to Use
- Optimal substructure (optimal solution built from optimal sub-solutions)
- Overlapping subproblems (same subproblem solved multiple times)
- Counting problems (number of ways)
- Optimization (min/max)

## Visual

### Fibonacci - The Classic Example
```
Recursive (without DP):

                    fib(5)
                   /      \
              fib(4)      fib(3)
             /    \       /    \
         fib(3)  fib(2) fib(2) fib(1)
         /   \
     fib(2) fib(1)

fib(3) calculated 2 times!
fib(2) calculated 3 times!

With DP (memoization):

fib(5) → cache miss, compute
  fib(4) → cache miss, compute
    fib(3) → cache miss, compute
      fib(2) → cache miss, return 1
      fib(1) → return 1
    fib(2) → cache HIT! return 1
  fib(3) → cache HIT! return 2

Each subproblem solved only once!
```

### Climbing Stairs
```
n = 4 stairs (can take 1 or 2 steps)

Ways to reach each stair:

Stair:    0    1    2    3    4
Ways:    [1]  [1]  [2]  [3]  [5]
          ↑    ↑    ↑
        base  base  dp[0]+dp[1]

dp[i] = dp[i-1] + dp[i-2]

Visual of paths to stair 4:
         ┌─→ 1 → 2 → 3 → 4
         │   └─→ 3 ─→ 4
    0 ───┼─→ 2 ─→ 3 → 4
         │       └─→ 4
         └─→ 2 → 4

5 total ways
```

### Longest Palindromic Substring
```
String: "babad"

DP table (is s[i:j+1] palindrome?):

    b  a  b  a  d
b   T  F  T  F  F
a      T  F  T  F
b         T  F  F
a            T  F
d               T

Diagonal = single chars (always true)
Check: s[i]==s[j] AND dp[i+1][j-1]

Longest found: "bab" or "aba" (length 3)
```

### 0/1 Knapsack Pattern
```
Items: [(weight=1, value=6), (w=2, v=10), (w=3, v=12)]
Capacity: 5

DP table (max value with capacity j using items 0..i):

         Capacity
         0   1   2   3   4   5
      ┌───────────────────────
    0 │  0   0   0   0   0   0
    1 │  0   6   6   6   6   6    (item: w=1, v=6)
    2 │  0   6  10  16  16  16    (item: w=2, v=10)
    3 │  0   6  10  16  18  22    (item: w=3, v=12)

dp[i][j] = max(
  dp[i-1][j],              // don't take item
  dp[i-1][j-w[i]] + v[i]   // take item (if fits)
)

Max value = 22 (items 1 and 3: 6 + 10 + 12... wait)
Actually: items with w=2,v=10 and w=3,v=12 = 22 ✓
```

## Template

### Python
```python
# Top-down (Memoization)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# Bottom-up (Tabulation)
def fib_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Space-optimized
def fib_optimized(n):
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1

# Climbing stairs
def climb_stairs(n):
    if n <= 2:
        return n

    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1

# Min cost climbing stairs
def min_cost_climbing(cost):
    n = len(cost)
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

    return dp[n]

# Longest palindromic substring
def longest_palindrome(s):
    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for length 2+
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if length == 2:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

            if dp[i][j] and length > max_len:
                start = i
                max_len = length

    return s[start:start + max_len]
```

### TypeScript
```typescript
// Top-down (Memoization)
function fibMemo(n: number, memo: Map<number, number> = new Map()): number {
  if (memo.has(n)) return memo.get(n)!;
  if (n <= 1) return n;

  const result = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
  memo.set(n, result);
  return result;
}

// Bottom-up (Tabulation)
function fibTab(n: number): number {
  if (n <= 1) return n;

  const dp = new Array(n + 1).fill(0);
  dp[1] = 1;

  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
}

// Climbing stairs
function climbStairs(n: number): number {
  if (n <= 2) return n;

  let prev2 = 1, prev1 = 2;
  for (let i = 3; i <= n; i++) {
    const curr = prev1 + prev2;
    prev2 = prev1;
    prev1 = curr;
  }

  return prev1;
}

// Min cost climbing stairs
function minCostClimbing(cost: number[]): number {
  const n = cost.length;
  const dp = new Array(n + 1).fill(0);

  for (let i = 2; i <= n; i++) {
    dp[i] = Math.min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
  }

  return dp[n];
}
```

## Approach
1. **Define state:** What does dp[i] represent?
2. **Find recurrence:** How does dp[i] relate to previous states?
3. **Base cases:** What are the starting values?
4. **Order of computation:** Bottom-up or top-down?
5. **Optimize space:** Can we use rolling array?

## Complexity
- **Time:** Usually O(n) or O(n²) depending on states
- **Space:** O(n) tabulation, often optimizable to O(1)

## Common Problems
- [x] Climbing Stairs
- [x] Min Cost Climbing Stairs
- [x] Longest Palindromic Substring
- [x] Best Time to Buy/Sell Stock with Fee
- [ ] House Robber
- [ ] Coin Change
- [ ] Longest Common Subsequence
