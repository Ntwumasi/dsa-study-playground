"""
Climbing Stairs (LeetCode 70)

PATTERN: Dynamic Programming - Linear 1D DP
- At each step, you can climb 1 or 2 stairs
- Count total distinct ways to reach the top
- This is essentially Fibonacci in disguise!

TIME COMPLEXITY: O(n) - single pass
SPACE COMPLEXITY: O(n) with array, O(1) optimized

WHY THIS IS FIBONACCI:
- To reach step n, you came from either step (n-1) or step (n-2)
- ways(n) = ways(n-1) + ways(n-2)
- Same recurrence as Fibonacci!
"""


def climb_stairs(n: int) -> int:
    """
    Count distinct ways to climb n stairs (1 or 2 steps at a time).

    Args:
        n: Number of stairs to climb

    Returns:
        Number of distinct ways to reach the top

    Visual:
        n = 4 stairs

        Ways to climb:
        1. 1+1+1+1 (four 1-steps)
        2. 1+1+2   (two 1-steps, one 2-step)
        3. 1+2+1
        4. 2+1+1
        5. 2+2     (two 2-steps)

        dp[1] = 1  (only one way: 1)
        dp[2] = 2  (two ways: 1+1 or 2)
        dp[3] = dp[2] + dp[1] = 3
        dp[4] = dp[3] + dp[2] = 5

        Answer: 5 ways
    """
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 2

    # dp[i] = number of ways to reach step i
    dp = [0] * (n + 1)
    dp[1] = 1  # One way to reach step 1: take one 1-step
    dp[2] = 2  # Two ways to reach step 2: 1+1 or 2

    # Fill DP array
    for i in range(3, n + 1):
        # To reach step i, either:
        # - Came from step (i-1) with a 1-step, OR
        # - Came from step (i-2) with a 2-step
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climb_stairs_optimized(n: int) -> int:
    """
    Space-optimized version using O(1) space.
    """
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev2 = 1  # ways to reach (i-2)
    prev1 = 2  # ways to reach (i-1)

    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


def climb_stairs_k_steps(n: int, k: int) -> int:
    """
    Generalization: Can take 1 to k steps at a time.

    dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-k]
    """
    if n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: 1 way to stay at ground (do nothing)

    for i in range(1, n + 1):
        for j in range(1, min(k, i) + 1):
            dp[i] += dp[i - j]

    return dp[n]


# Test cases
if __name__ == "__main__":
    # Basic cases
    print(f"Stairs=1: {climb_stairs(1)} ways")  # 1
    print(f"Stairs=2: {climb_stairs(2)} ways")  # 2
    print(f"Stairs=3: {climb_stairs(3)} ways")  # 3
    print(f"Stairs=4: {climb_stairs(4)} ways")  # 5
    print(f"Stairs=5: {climb_stairs(5)} ways")  # 8

    # Verify optimized version
    print(f"\nOptimized stairs=10: {climb_stairs_optimized(10)} ways")  # 89

    # Generalized k-steps
    print(f"\nWith 1-3 steps, stairs=4: {climb_stairs_k_steps(4, 3)} ways")  # 7

    """
    INTUITION:

    Think of it as: "How did I get to step n?"

    Either:
    1. I was at step (n-1) and took 1 step
    2. I was at step (n-2) and took 2 steps

    So: ways(n) = ways(n-1) + ways(n-2)

    This is exactly the Fibonacci recurrence!

    F:    0, 1, 1, 2, 3, 5, 8, 13, 21...
    Stairs: 1, 2, 3, 5, 8, 13, 21... (shifted by 1)
    """
