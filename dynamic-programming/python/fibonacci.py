"""
Fibonacci Number (LeetCode 509)

PATTERN: Dynamic Programming - Basic 1D DP
- Compute F(n) where F(n) = F(n-1) + F(n-2)
- Classic DP example: overlapping subproblems + optimal substructure

TIME COMPLEXITY: O(n) - compute each value once
SPACE COMPLEXITY: O(n) with array, O(1) with space optimization

WHY DP WORKS HERE:
- Recursive solution has exponential time due to repeated calculations
- F(5) = F(4) + F(3), F(4) = F(3) + F(2) -> F(3) calculated twice!
- DP stores computed values to avoid recalculation
"""


def fibonacci_dp(n: int) -> int:
    """
    Calculate the nth Fibonacci number using tabulation (bottom-up DP).

    Args:
        n: Index in Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number

    Visual:
        F(0) = 0
        F(1) = 1
        F(2) = F(1) + F(0) = 1
        F(3) = F(2) + F(1) = 2
        F(4) = F(3) + F(2) = 3
        F(5) = F(4) + F(3) = 5
        F(6) = F(5) + F(4) = 8

        dp = [0, 1, 1, 2, 3, 5, 8]
    """
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Create DP array
    dp = [0] * (n + 1)
    dp[1] = 1  # Base case: F(1) = 1

    # Fill DP array from bottom up
    for i in range(2, n + 1):
        # Recurrence relation: F(n) = F(n-1) + F(n-2)
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fibonacci_optimized(n: int) -> int:
    """
    Space-optimized version using O(1) space.

    We only need the previous two values, not the entire array.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev2 = 0  # F(n-2)
    prev1 = 1  # F(n-1)

    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


def fibonacci_recursive_memo(n: int, memo: dict = None) -> int:
    """
    Memoized recursive solution (top-down DP).

    Same time complexity as tabulation, but uses recursion.
    """
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_recursive_memo(n - 1, memo) + fibonacci_recursive_memo(n - 2, memo)
    return memo[n]


# Test cases
if __name__ == "__main__":
    print("Fibonacci sequence (first 10 numbers):")
    for i in range(10):
        print(f"F({i}) = {fibonacci_dp(i)}")

    # Verify all methods give same result
    print(f"\nF(20) using tabulation: {fibonacci_dp(20)}")
    print(f"F(20) using optimization: {fibonacci_optimized(20)}")
    print(f"F(20) using memoization: {fibonacci_recursive_memo(20)}")

    """
    TIME COMPLEXITY COMPARISON:

    1. Naive Recursion: O(2^n) - exponential, very slow!
       def fib(n):
           if n <= 1: return n
           return fib(n-1) + fib(n-2)  # Repeated work!

    2. Memoization (Top-Down): O(n) time, O(n) space
       - Recursive but caches results
       - Computes only what's needed

    3. Tabulation (Bottom-Up): O(n) time, O(n) space
       - Iterative, fills table from base cases
       - Often faster due to no recursion overhead

    4. Space Optimized: O(n) time, O(1) space
       - Only stores what we need (last 2 values)
       - Best overall for this problem
    """
